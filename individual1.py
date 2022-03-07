#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое число, целая часть числа; поле second — положительное целое число,
дробная часть числа. Реализовать метод multiply() — умножение на произвольное целое
число типа int. Метод должен правильно работать при любых допустимых значениях first и
second.
"""

class Real:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if (self.first <= 0) or (self.second <= 0):
            raise ValueError()

    def read(self):
        self.first = int(input("Введите целую часть числа "))
        self.second = int(input("Введите дробную часть числа "))

    def __str__(self):
        return f"{self.first} / {self.second}"

    def __repr__(self):
        return self.__str__()

    def display(self):
        print(f"Число с плавающей точкой {self.first}.{self.second}")

    def __mul__(self, other):  # *
        self.first = self.first * other
        self.second = (self.second / 10) * other
        print("Результат умножения - ", self.first + self.second)


if __name__ == '__main__':
    t1 = Real(12, 5)
    t2 = Real(6, 5)
    t1.display()
    print(t1 * 5)
