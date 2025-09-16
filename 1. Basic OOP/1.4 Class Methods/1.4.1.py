class MediaPlater:
    def open(self, file) -> None:
        self.filename = file

    def play(self) -> None:
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlater()
media2 = MediaPlater()
media1.open("filemedia1")
media1.play()
media2.open("filemedia2")
media2.play()
print(MediaPlater.__dict__)