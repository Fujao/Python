valor = float(input('Valor? R$ '))
tempo = float(input('Tempo do investimento? '))
selic = float(input('Valor da selic? (%) '))
opcao = input('Qual investimento (P/C)? ')
if opcao == 'P':
    if selic <= 8.5:
        premio = 0.70 * (selic/100/12) * (tempo//30) * valor
    else:
        premio = 0.005 * (tempo//30) * valor
        
else:
    cdi = selic = 0.1
    premio =(cdi/100/360) * tempo * valor
    if tempo <= 180:
        ir = premio * 0.225
    elif tempo <= 360:
        ir = premio * 0.20
    elif tempo <= 720:
        ir = premio * 0.175
    else:
        ir = premio * 0.15
    premio -= ir
print(f'Premio: R$ {premio:.2f}')    



