# Создаем массив C
C = [3, 7, 2, 8, 5, 10, 9, 12, 1, 6, 4]

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