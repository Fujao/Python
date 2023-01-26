dicionario = {}

for i in range(5):
    nome_produto = input('Nome do produto: ')
    preco = float(input('Preco do produto: '))
    dicionario[nome_produto] = preco


print('-'*10)
print('Lista de produtos')
print(dicionario)
print('-'*10)

for nome_produto, preco in dicionario.items():
    if preco > 50.0:
        print(nome_produto)
        
