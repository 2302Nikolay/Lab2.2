#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input("Введите три числа: "))
b = int(input())
c = int(input())

if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
    print("Одо из чисел четное.")
else:
    print("Среди введенных чисел нет четных чисел.")
