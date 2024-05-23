C = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

chetniy = 0
nechetniy = 0

for i, element in enumerate(C):
        if i % 2 == 0:
                chetniy += element
        else:
                nechetniy += element
print('Массив С:', C)

print("Сумма четных :", chetniy)
print("Сумма нечетных:", nechetniy)

if chetniy > nechetniy:
        print("Большая сумма: sum_even_index =", chetniy)
else:
        print("Большая сумма: sum_odd_index =", nechetniy)
