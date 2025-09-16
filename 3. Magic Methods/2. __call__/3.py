class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, file: str,  *args, **kwargs):
        s = file.split('.')[1]
        return s in self.extensions


filenames = ['boat.jpg', 'text.txt', 'python.doc']
ex = ('jpg', 'doc')
acceptor = ImageFileAcceptor(ex)
print(*filter(acceptor, filenames))