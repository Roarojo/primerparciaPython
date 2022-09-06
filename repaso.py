def validar(p):
    #b2=False
    #if (b==False):
    if a[p]==0:
        arreglo(p)
           

def arreglo(q):
    ban=True
    n = int(input('Escribe un numero diferente de 0'))
    if (a[q]==0):
        if ((q%2)==0 and (n%2)==0):
            a[q]=n
        if ((q%2)!=0 and (n%2)!=0):
            a[q]=n
        if a[q]==0:
            #arreglo(q)
            #ban=False
            validar(q)
    
a =[0,0,0,0,0,0,0,0,0,0]
for x in range(0,10):
    arreglo(x)
    print(x,' ',a[x])

