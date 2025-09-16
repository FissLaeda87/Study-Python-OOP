class Model:
    def query(self, **kwargs):
        self.info = kwargs

    def __str__(self):
        return 'Model: ' + ', '.join([f'{k} = {v}' for k, v in self.info.items()])

model = Model()
model.query(id = 1, fio = "Sergey", old = 33)
print(model)