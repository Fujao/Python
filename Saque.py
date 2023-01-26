def withdraw(conta1, valor):
    conta1 -= valor
    return conta1


def transfer(conta2, valor):
    conta2 += valor
    return conta2


hash_account = input('Account 1: ')
hash_account_2 = input('Account 2: ')
conta1 = float(input('Saldo da primeira account: '))
conta2 = float(input('Saldo da segunda account: '))
valor = float(input('Quantidade de saque: '))

print()
print('-'*20)
print(f'Valor do saldo antes da transferencia conta1: {conta1}')
print('-'*20)
print(f'Valor do saldo antes da transferencia conta2: {conta2}')
print('-'*20)
print()

amount2 = withdraw(conta1, valor)
amount1 = transfer(conta2, valor)

print()
print('-'*20)
print(f'Valor do saldo depois da transferencia conta1: {amount2:.2f}')
print('-'*20)
print()
print('-'*20)
print(f'Valor do saldo depois da transferencia conta2: {amount1:.2f}')
print('-'*20)
print()