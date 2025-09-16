class Clock:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def get_time(self):
        return self.h * 3600 + self.m * 60 + self.s

class DeltaClock:
    def __init__(self, t2: Clock, t1: Clock):
        self.t2 = t2
        self.t1 = t1

    def __len__(self):
        dt = self.t2.get_time() - self.t1.get_time()
        if dt >= 0:
            return dt
        else:
            return 0

    def __repr__(self):
        dt = self.t2.get_time() - self.t1.get_time()
        h = dt // 3600
        dt = dt - h *  3600
        m = dt // 60
        s = dt % m if m > 0 else dt
        print(f"{h} : {m} : {s}")

    def __str__(self):
        dt = self.t2.get_time() - self.t1.get_time()
        h = dt // 3600
        dt = dt - h *  3600
        m = dt // 60
        s = dt % m if m > 0 else dt
        return f"{h:02} : {m:02} : {s:02}"

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(str(dt))
print(len(dt))
print(dt)