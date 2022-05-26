#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    c = int(input("Введите число: "))

    if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
        print("Одно из чисел четное.")
    else:
        print("Среди введенных чисел нет четных чисел.")
