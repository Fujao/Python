from fila import *

fp1 = Fila(10) # Prioridade máxima
fp2 = Fila(10) # Prioridade média
fp3 = Fila(10) # Prioridade mínima

nome = input('Nome? ')
while nome != '':
    prioridade = int(input('Prioridade? '))
    if prioridade == 1:
        fp1.enfileira((nome, prioridade))
    elif prioridade == 2:
        fp2.enfileira((nome, prioridade))
    else:
        fp3.enfileira((nome, prioridade))
    print()
    nome = input('Nome? ')

while not fp1.vazia() or not fp2.vazia() or not fp3.vazia():
    if not fp1.vazia():
        print(f'Atendeu: {fp1.desenfileira()}')
    elif not fp2.vazia():
        print(f'Atendeu: {fp2.desenfileira()}')
    else:
        print(f'Atendeu: {fp3.desenfileira()}')

print('Atendimento encerrado!')
