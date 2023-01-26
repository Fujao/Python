ano1 = int(input())
ano2 = int(input())

x = 0

for y in range(ano1, ano2+1):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        print(y)
        x += 1
print(f'Bissextos: {x}')
