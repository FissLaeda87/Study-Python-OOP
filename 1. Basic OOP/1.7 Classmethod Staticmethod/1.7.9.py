class Video:

    def create(self, name):
        self.name = name

    def play(self):
        print(f"Воспроизведение видео: {self.name}")

class YouTube:
    VIDEOS = []

    @classmethod
    def add_video(cls, video: Video):
        cls.VIDEOS.append(video)

    @classmethod
    def play(cls, video_index):
        cls.VIDEOS[video_index].play()

v1 = Video()
v1.create("Python")
v2 = Video()
v2.create("Python OOP")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
