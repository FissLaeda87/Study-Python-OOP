from  string import ascii_uppercase, digits


class CardCheck:
    NAME_SET = set(ascii_uppercase + digits)

    @classmethod
    def chek_name(cls, name):
        if not isinstance(name, str):
            return False
        s = name.split()
        if len(s) != 2:
            return False
        return all(map(lambda x: set(x) < cls.NAME_SET, s))

    @staticmethod
    def check_card(card):
        if type(card) != str:
            return False
        card_list = card.split('-')
        if len(card_list) != 4:
            return False
        return all(map(lambda x: x.isdigit() and len(x) == 4, card_list))

print(CardCheck.check_card('1232-1234-1234-1234'))
print(CardCheck.chek_name('DENIS FISENKO'))