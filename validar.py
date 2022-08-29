from curses.ascii import isalnum, isalpha, isdigit

def validarletras(a):
    x = 0
    for i in a:
        if isalpha(i):
            print('es una letra')
        else:
            print('No es caracte')
        

a = input('Escribe un nombre')
validarletras(a)