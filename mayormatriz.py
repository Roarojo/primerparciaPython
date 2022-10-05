def validar():
    a = input('Escriber un numero')
    if len(a)==2:
        if a.isdigit():
            return a
        else:
            print('error')
            return validar()
    else:
        print('error')
        return validar()

def llenar():
    for x in range(3):
        for y in range(2):
            ar[x][y] = int(validar())


def mayor():
    aux = 0
    for x in range(3):
        for y in range(2):
            if aux<ar[x][y]:
                aux = ar[x][y]
    print('El mayor es: ',aux)


ar = [[0,0],[0,0],[0,0]]
llenar()
for i in ar:
    print(i)
mayor()
print('La matriz es: ',len(ar))#muestra al numero de renglones de la matriz
print('La matriz es: ',len(ar[0]))#muestra el numero de columnas de la matriz