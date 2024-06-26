import numpy as np

S = 23
G = 7
S = S / 10
G = G / 10

a0 = -S * (G**2 + S**2)
a1 = (G + S) ** 2
a2 = -(2 * G - S)
a3 = 1

def f(x):
    return a0 + a1 * x + a2 * a2 + a3 * a3

def rectangle_method(a, b, n):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n)) * h
    return result

def trapezoid_method(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) / 2
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

def simpson_method(a, b, n):
    h = (b - a) / n
    result = (f(a) + f(b)) + 4 * sum(f(a + (2 * i - 1) * h) for i in range(1, n // 2 + 1)) + 2 * sum(
        f(a + 2 * i * h) for i in range(1, n // 2))
    result *= h / 3
    return result

a = 0
b = 3
n = 1000

S_rect = rectangle_method(a, b, n)
S_trap = trapezoid_method(a, b, n)
S_simp = simpson_method(a, b, n)

print(f"Метод прямоугольников: {S_rect}")
print(f"Метод трапеций: {S_trap}")
print(f"Метод Симпсона: {S_simp}")