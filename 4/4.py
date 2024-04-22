import numpy as np
import matplotlib.pyplot as plt

a0 = 2
a1 = 16
a2 = 27
a3 = 40
a4 = 4

# функция
y = lambda x: a0*x**4-a1*x**3+a2*x**2+a3*x-a4
print("y:", y)

# создаѐм область, в которой будет
# - отображаться график
x = np.linspace(-5, 5, 42)
print(' x y(x)')
for temp in x :
    print ( temp, y(temp))

xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')

fmax = max(y(x))
print('Ymax = ',fmax)

xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')

fmin = min(y(x))
print('Ymin = ',fmin)

# создаѐм рисунок с координатную плоскость
fig = plt.subplots()

# значения x, которые будут отображены
# количество элементов в созданном массиве
# - качество прорисовки графика
# рисуем график
plt.plot(x, y(x))

# показываем график
plt.show()