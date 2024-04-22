import random

# Генерируем случайный массив C длиной от 1 до 25 элементов
C = [random.randint(1, 20) for _ in range(random.randint(1, 25))]

# Проверяем длину массива C
if len(C) <= 25:
    print("Количество элементов в массиве C не превышает 25.")
else:
    print("Количество элементов в массиве C превышает 25.")

# Инициализируем переменные для сумм четных и нечетных элементов
sum_even = 0
sum_odd = 0

# Суммируем элементы с четными и нечетными номерами
for i in range(len(C)):
    if i % 2 == 0:
        sum_even += C[i]
    else:
        sum_odd += C[i]

# Определяем большую сумму
if sum_even > sum_odd:
    largest_sum = sum_even
    largest_sum_type = "четных элементов"
else:
    largest_sum = sum_odd
    largest_sum_type = "нечетных элементов"

# Выводим исходный массив, суммы и определяем, какая сумма больше
print("Исходный массив C:", C)
print("Сумма элементов с четными номерами:", sum_even)
print("Сумма элементов с нечетными номерами:", sum_odd)
print(f"Большая сумма: {largest_sum} (сумма {largest_sum_type})")