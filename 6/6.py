import random

m = 25

C = [random.randint(1, 100) for _ in range(m)]

chet = sum(C[i] for i in range(0, m, 2)) # - (начало,конец,шаг)

NEchet = sum(C[i] for i in range(1, m, 2))

if chet > NEchet:
    summa = chet
else:
    summa = NEchet

print("Массив C:", C)
print("Большая сумма:", summa)
