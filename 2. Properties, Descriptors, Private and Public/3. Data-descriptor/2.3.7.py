class ValidateString:
    def __init__(self, min, max):
        self.min_length = min
        self.max_length = max

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, valid: ValidateString):
        self.validator = valid

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class RegisterForm:
    login = StringValue(ValidateString(1, 20))
    password = StringValue(ValidateString(5, 10))
    email = StringValue(ValidateString(8, 50))

    def __init__(self, l, p, e):
        self.login = l
        self.password = p
        self.email = e

    def det_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f"""<form>
            Логин: {self.login}
            Пароль: {self.password}
            Email: {self.email}
            </form>
            """)

form = RegisterForm("Денис", "12345", "Fiss_Laeda87@mail.ru")
form.det_fields()
form.show()