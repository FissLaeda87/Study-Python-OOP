from string import ascii_letters, digits
from random import choice, randint

class RandomPassword:
    def __init__(self, chars: str, min_length, max_length):
        self.psw_chars = chars
        self.min_length = min_length
        self.max_length = max_length


    def __call__(self, *args, **kwargs):
        length = randint(self.min_length, self.max_length)
        return "".join([choice(self.psw_chars) for _ in range(length)])

psw = RandomPassword(ascii_letters+digits, 5, 20)
print([psw() for _ in range(3)])

