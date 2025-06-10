import stanza
import os

# 1. 한국어 문장 토크나이저 로딩
nlp = stanza.Pipeline('ko', processors='tokenize', use_gpu=False)

# 2. 문장 경계 구하기
def get_sentence_boundaries(text):
    doc = nlp(text)
    boundaries = []
    offset = 0
    for sent in doc.sentences:
        sent_text = sent.text
        start = text.find(sent_text, offset)
        end = start + len(sent_text)
        boundaries.append((start, end))
        offset = end
    return boundaries

# 3. 청크 나누기
def chunk_text(text, boundaries, start_hint_list, max_chunk_size):
    chunks = []
    for start_hint in start_hint_list:
        # (1) 시작 후보 문장 찾기
        possible_starts = [s for (s, e) in boundaries if s >= start_hint]
        if not possible_starts:
            break
        start = possible_starts[0]

        # (2) 최대 크기 내에서 끝낼 수 있는 문장 찾기
        possible_ends = [e for (s, e) in boundaries if s >= start and (e - start) <= max_chunk_size]
        if not possible_ends:
            break
        end = possible_ends[-1]

        chunk = text[start:end].strip()
        chunks.append(chunk)
    return chunks

# 4. start_hints 자동 생성 (2000 간격, 끝 범위 초과시 중단)
def generate_start_hints(text_length, step=2000):
    hints = []
    n = 0
    while True:
        hint = step * n
        if hint + step > text_length:
            break
        hints.append(hint)
        n += 1
    return hints

# 5. 전체 실행
def split_text_into_chunks(file_path, max_chunk_size=4000, step=8000):
    with open(file_path, 'r', encoding='utf-8') as f:
        full_text = f.read()

    boundaries = get_sentence_boundaries(full_text)
    start_hints = generate_start_hints(len(full_text), step=step)
    chunks = chunk_text(full_text, boundaries, start_hints, max_chunk_size=max_chunk_size)

    return chunks

# 6. 실행 예시
if __name__ == '__main__':
    file_path = file_path = os.path.join(os.path.dirname(__file__), 'example.txt')
    chunks = split_text_into_chunks(file_path)

    for i, chunk in enumerate(chunks):
        print(f'--- Chunk {i+1} ({len(chunk)} chars) ---')
        print(chunk)
        print()