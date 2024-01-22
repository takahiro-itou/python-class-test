#!/usr/bin/python3

class HogeA:
    def __init__(self, v):
        print('Init HogeA')
        self.value = v

    def print_value(self):
        print("HogeA : value = {0}".format(self.value,))

class FugaB:
    def __init__(self, v):
        print('Init FugaB')
        self.value = v

    def print_value(self):
        print("FugaB : value = {0}".format(self.value,))

def instantiate(cls, val):
    return  cls(val)

x1 = instantiate(HogeA, 1234)
x1.print_value()

x2 = instantiate(FugaB, 555)
x2.print_value()


print(globals())
y = eval('HogeA')
print(y)
