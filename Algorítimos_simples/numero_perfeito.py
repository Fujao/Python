def divisivel(x, y):
    return x % y == 0

def perfeito(x):
    soma = 0
    for divisor in range(1, x):
        if divisivel(x, divisor):
            soma += divisor
    return soma == x
       
n = int(input())
for i in range(n):
    x = int(input())
    if perfeito(x):
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')
