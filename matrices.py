
from time import sleep


a=[[0,0,0],
   [0,0,0],
   [0,0,0]]
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]

for x in range(3):
    for y in range(3):
        b = int(input('Escribe un numero'))
        a[x][y]=b

c = int(input('Escribe un escalar'))
for x in range(3):
    for y in range(3):
        res[x][y]= a[x][y] * c

for x in range(3):
    for y in range(3):
        print(a[x][y],end=' ')
        sleep(1)
    print()

for x in range(3):
    for y in range(3):
        print(res[x][y],end=' ')
        sleep(1)
    print()


'''for m in a:
    print(m)
    sleep(1)'''