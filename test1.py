#!/usr/bin/python3

class HogeA:
    def __init__(self, v):
        print('Init HogeA')
        self.value = v

    def print_value(self):
        print("HogeA : value = {0}".format(self.value,))

def instantiate(cls, val):
    return  cls(val)

x1 = instantiate(HogeA, 1234)
