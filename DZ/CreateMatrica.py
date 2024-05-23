
import numpy as np
rows = 5
cols = 5
# задали строки и столбцы
matrix = np.random.randint(-25, 26, size=(rows, cols))

# Открываем файл для записи
with open('matrica.txt', 'w') as file:
    # Перебираем каждую строку матрицы
    for row in matrix:
        # Преобразуем строку в строку, разделяя элементы пробелами
        row_str = ' '.join(map(str, row))
        # Записываем строку в файл
        file.write(row_str + '\n')

print("Матрица создана 'matrica.txt'.")