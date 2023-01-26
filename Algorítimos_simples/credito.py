credito = float(input('Crédito? '))
total = 0
posicao = 1
preco = float(input(f'Preço do item {posicao}? '))
while credito >= preco:
    total += preco
    credito -= preco
    posicao += 1
    preco = float(input(f'Preço do item {posicao}? '))
    if preco > credito:
        print(f'Compra do item {posicao} negada!')
print(f'Itens comprados: {posicao-1}')
print(f'Total da compra: R$ {total:.2f}')
print(f'Crédito restante: R$ {total:.2f}')
