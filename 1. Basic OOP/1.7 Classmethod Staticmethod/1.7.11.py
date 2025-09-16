class Message:
    def __init__(self, msg):
        self.text = msg
        self.like = False

class Viber:
    MESSAGES: dict = dict()

    @classmethod
    def add_message(cls, msg: Message):
        if id(msg) not in cls.MESSAGES:
            cls.MESSAGES[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg: Message):
        if id(msg) in cls.MESSAGES:
            cls.MESSAGES.pop(id(msg))

    @classmethod
    def set_like(cls, msg: Message):
        if id(msg) in cls.MESSAGES:
            cls.MESSAGES[id(msg)].like = not cls.MESSAGES[id(msg)].like

    @staticmethod
    def total_messages():
        return len(Viber.MESSAGES)

msg = Message("Hello all!")
Viber.add_message(msg)
Viber.add_message(Message("I am Denis"))
Viber.set_like(msg)
print(msg.like)
print(Viber.total_messages())
Viber.remove_message(msg)
print(Viber.total_messages())