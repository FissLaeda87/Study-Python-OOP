from random import choices, randint, choice
from string import digits, ascii_lowercase

class EmailValidator:
    __CHARS = ascii_lowercase + digits + "_"
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email = choices(ascii_lowercase + digits, k = 10)
        email.append('@')
        email.append(choice(["mail.ru", "gmail.com", "yandex.ru"]))
        return "".join(email)

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False
        if email.count('@') != 1 or email.count('..'):
            return False
        s1, s2 = email.split("@")
        if len(s1) > 100 or len(s2) > 50:
            return False
        if s2.count('.') < 1:
            return False
        if not set(email) <= set(cls.__CHARS + '@' + '.'):
            return False
        return True

res = EmailValidator()
print(res)
res = EmailValidator.get_random_email()
print(res)
print(EmailValidator.check_email(res))
print(res)
print(EmailValidator.check_email('sc_lib@sc_lib_ru'))
print(EmailValidator.check_email(1))
