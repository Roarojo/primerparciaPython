def validar(b):
    for x in v:
        print(x," ",b)
        if b==x:
            b = input("escribe un dato")
            validar(b)
    return b 

p =0
v = [" "," "," "," "]
while(p<=4):
    a = input("escribe un dato")
    a = validar(a)
    if len(a)==1:
        if a=='a':
            v[p]=a
        if a=='e':
            v[p]=a
        if a=='i':
            v[p]=a
        if a=='o':
            v[p]=a
        if a=='u':
            v[p]=a
        p += 1