class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.x = to_x
        self.y = to_y
        self.__speed = max_speed


class Track:
    def __init__(self, x, y):
        self._start_x = x
        self._start_y = y
        self._tracks: list[TrackLine] = []

    def add_track(self, tr: TrackLine):
        self._tracks.append(tr)

    def get_tracks(self):
        return tuple(self._tracks)

    def __get_length(self, i):
        return ((self._tracks[i].x - self._tracks[i-1].x)**2 + (self._tracks[i].y - self._tracks[i-1].y)**2)**0.5

    def __len__(self):
        l_start = ((self._tracks[0].x - self._start_x)**2 + (self._tracks[0].y - self._start_y)**2)**0.5
        res = sum(self.__get_length(i) for i in range(1, len(self._tracks)))
        return int(l_start + res)

    def __eq__(self, other: TrackLine):
        return len(self) == len(other)

    def __lt__(self, other: TrackLine):
        return self.__len__() < other.__len__()

tr1 = Track(0, 0)
tr2 = Track(0, 1)
tr1.add_track(TrackLine(2, 4, 100))
tr1.add_track(TrackLine(5, -4, 100))
tr2.add_track(TrackLine(3, 2, 90))
tr2.add_track(TrackLine(10, 8, 90))
print(len(tr1))
print(len(tr2))
print(tr1 == tr2)
print(tr1 > tr2)
