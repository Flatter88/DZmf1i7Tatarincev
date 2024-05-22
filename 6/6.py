import random

m = 15
A = [random.randint(1, 100) for _ in range(m)] # - _ это не важное имя переменной
B = [random.randint(1, 100) for _ in range(m)]
K = [1 if A[i] > B[i] else 0 for i in range(m)]

print("Массив A:", A)
print("Массив B:", B)
print("Массив K:", K)
