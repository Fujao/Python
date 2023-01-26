from random import randint

def misterio(L):
    for i in range(len(L)):
        L[i] =L[i] * 2

def aleatoria(qtd):
    L = []
    for i in range(qtd):
        L.append(randint(1, 5))
    return L

L = aleatoria(7)

print('L:', L)
misterio(L)
print('L:', L)


