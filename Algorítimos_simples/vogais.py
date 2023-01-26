x = {}
vogais = ['a', 'e', 'i', 'o', 'u']

for i in vogais:
    x[i] = 0


y = input()

for a in y.lower():
    if a in vogais:
        x[a] += 1

for i in vogais:
    print(i, " = ", x[i])
        
