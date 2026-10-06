def retornarMaiorNumero(a, b, c):
    maior = a
    if(maior < b):
        maior = b
    if(maior < c):
        maior = c
    return maior
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(retornarMaiorNumero(a,b,c))