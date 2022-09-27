from time import sleep
def llenar(x):
    a = int(input('Escribe un numero'))
    arr.append(a)
    x += 1
    if x < 5:
        llenar(x)

def mostrar():
    for x in range(0,len(arr)):
        print(x," ",arr[x],"\n")

def pila():
    aux = len(arr)-1
    for x in range(0,len(arr)):
        sleep(3)
        arr.pop(aux)
        aux -=1
        print("Pila")
        print(arr)
def cola():
    for x in range(0,len(arr)):
        sleep(2)
        arr.pop(0)
        print("Cola")
        print(arr)

        


def liberarArreglo():
    valor = int(input('Escribe la posicion a eliminar'))
    if valor>=0 and valor<len(arr):
        arr.pop(valor)
    else:
        print('Posicion incorrecta')

x = 0
arr = []
res = "si"
llenar(x)
mostrar()
#pila()
cola()

'''while(res=="si"):
    liberarArreglo()
    mostrar()
    res = input('Deseas otro ejecusion si/no')'''



