class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu: CPU, *args: Memory):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots: list[Memory] = list(args) if len(args) <= self.total_mem_slots else list(args[0:self.total_mem_slots])

    def get_config(self):
        s = [
            f"Материнская плата - {self.name}",
            f"Центральный процессор - {self.cpu.name}, {str(self.cpu.fr)} ГЦ",
            f"Слотов памяти - {len(self.mem_slots)}",
            f"Память: {[' - '.join([slot.name, str(slot.volume)]) for slot in self.mem_slots]}"
        ]
        return s

mb = MotherBoard("Гигабайт 86 АТ", CPU('Intel i7 12700k', 3800), Memory('Kingston', 16), Memory('Kingston', 16))
print(mb.get_config())