# Programa para multiplicar matrices
# 3x3 matrix
from time import sleep

X = [[1,1,1],
    [1 ,1,1],
    [1 ,1,1]]
# 3x4 matrix
Y = [[5,8,10,2],
    [6,7,3,10],
    [4,5,9,10]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for i in X:
    print(i)
    sleep(1)

for i in Y:
    print(i)
    sleep(1)


for r in result:
   print(r)
   sleep(1)