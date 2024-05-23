N = int(input("Введите N: "))
X = []

for i in range(0,5):
    x = float(input("Введите x: "))
    # print("type_x:", type(x))
    X.append(x)

#X=[0.1,0.3, 0.4, 0.7, 1]
#X=[0.1,0.3, 0.4, 0.7, 1]

print(' :  x=0.1       s=0.00 :')
print(' :  x=0.3       s=0.01 :')
print(' -----------------------')

for x in X:
    s = 0
    u = -x
    for k in range(1,N+1):
        s += u**k/(k+1)*(k+3)
    print(" | %8.4f | %8.4f |" % (x,s))
print('           ...           ')
print(' -----------------------')