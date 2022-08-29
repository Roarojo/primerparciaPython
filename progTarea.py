def mostrar(n,e,s):
    if e>=18:
        if s=='M' or s=='m':
            print('Hombre')
    elif e<18:
        if s=='M' or s=='m':
            print('Niño')

n = input('Escribe el nombre \n')
s= input('Escribe el sexo M/F \n')
e = int(input('Escribe la edad'))
mostrar(n,e,s)


