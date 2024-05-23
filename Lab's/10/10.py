import numpy as np
s=23
g=7
N = 23
p=2*(g+s)
m = -p+s
A = [[p/6, m/6, 2*s],[m/6, 2*p+s/6, m/6],[2*s, m, p/6]]

print('Исходный массив A')
print(A)
print('Исходный массив A')

for i in range (0,N):
    for j in range (0,N):
        print('%f'%A[i][j], end=' ')
    print('')

L, X = np.linalg.eig(A)

print('Собственные значения A')
print(L)
print('Собственные векторы A')

for i in range (0,N):
    for j in range (0,N):
        print('%f'%X[i][j], end=' ')
    print('')