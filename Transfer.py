def verification(validador, status, transfer_amount):
    if status == 'Approve':
        for hash_account, amount_account in validador.items():
            if hash_account == 12345678:
                amount_account -= transfer_amount
                return amount_account
    else:
        print('Error x0x0x0x0')

def verification2(validador2, status, transfer_amount):
    if status == 'Approve':
        for hash_account2, amount_account2 in validador2.items():
            if hash_account2 == 1011121314:
                amount_account2 += transfer_amount
                return amount_account2
    else:
        print('Error x0x0x0x0')
                
    
validador = {}
validador2 = {}

hash_account = int(input('Wallet 1: '))
amount_account = 1000.0
validador[hash_account] = amount_account



hash_account2 = int(input('Wallet 2: '))
amount_account_2 = 500.0
validador2[hash_account2] = amount_account_2
    

transfer_amount = float(input('Transfer amount: '))
status = input('Approve transfer (Approve) / (Decline): ')


tudo = verification(validador, status, transfer_amount)
tudo2 = verification2(validador2, status, transfer_amount)

print()
print('-'*20)
print(f'Balance wallet1: {tudo}')
print('-'*20)
print()
print('-'*20)
print(f'Balance wallet2: {tudo2}')
print('-'*20)
print()