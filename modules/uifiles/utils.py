@staticmethod
def time_to_sec(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

@staticmethod
def sec_to_time(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"