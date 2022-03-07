#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

"""
Создать класс BitString для работы с битовыми строками не более чем из 100 бит. Битовая
строка должна быть представлена списком типа int, каждый элемент которого принимает
значение 0 или 1. Реальный размер списка задается как аргумент конструктора
инициализации. Должны быть реализованы все традиционные операции для работы с
битовыми строками: and, or, xor, not. Реализовать сдвиг влево и сдвиг вправо на заданное
количество битов.
"""

class BitString:

    def __init__(self, other=10):
        CONST_SIZE = 100
        self.other = other
        if CONST_SIZE > self.other:
            self.b = [randint(0, 1) for i in range(self.other)]
            self.number = int(''.join(map(str, self.b)))

    def display(self):
        print(f"Битовое число {self.number}")

    def __getitem__(self, key):
        return self.number[key]

    def __setitem__(self, key, value):
        self.number[key] = value
        return self.number

    def size(self):
        print(f"Длина числа {self.other}")

    def __and__(self, other):
        return print(f"Результат вычисления иключающее ИЛИ {self.number & other.number}")

    def __xor__(self, other):
        return print(f"Результат вычисления иключающее ИЛИ {self.number ^ other.number}")

    def __or__(self, other):
        return print(f"Результат вычисления ИЛИ {self.number | other.number}")

    def __lshift__(self, other):
        return print(f"Результат вычисления сдвига налево {self.number << other}")

    def __rshift__(self, other):
        return print(f"Результат вычисления сдвига направо {self.number >> other}")

    def __invert__(self):
        return ~self.number


if __name__ == '__main__':
    new = BitString(15)
    new2 = BitString(15)
    new & new2
    new >> 4
    new << 4
    new | new2
    new.size()
    new.display()
    new2.display()
