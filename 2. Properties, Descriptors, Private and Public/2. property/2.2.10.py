class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

class PhoneBook:
    def __init__(self):
        self.data = []

    def add_phone(self, phone: PhoneNumber):
        self.data.append(phone)

    def remove_phone(self, index):
        if self.data and len(self.data) < index:
            self.data.pop(index)

    def get_phone_list(self):
        return self.data