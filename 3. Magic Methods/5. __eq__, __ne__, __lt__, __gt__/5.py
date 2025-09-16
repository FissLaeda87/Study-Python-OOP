stich = ["Я Вам пишу - чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в Вашей воле",
         "Меня презреньем наказать.",
         "Но Вы, к моей несчастной доле",
         "Хоть каплю жалости храня",
         "Вы не оставите меня"]

stich = [[word.strip('-?!,.; ') for word in st.split()]  for st in stich]
print(stich)

class StringText:
    def __init__(self, lst_word):
        self.lst_word = lst_word

    def __len__(self):
        return len(self.lst_word)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) < len(other)

lst_text = [StringText(st) for st in stich]
lst_text_sorted = sorted(lst_text, key=lambda x: len(x), reverse=True)
lst_text_sorted = [" ".join(l.lst_word) for l in lst_text_sorted]
print(lst_text_sorted)