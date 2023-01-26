vote = {}
blank_votes = 0

for _ in range(5):
    name_candidate = input('INSIRA O NOME DO CANDIDATO: ')
    number_candidate = int(input('INSIRA O NUMERO DO CANDIDATO: '))
    vote_candidate = 0
    vote[number_candidate] = [name_candidate, vote_candidate]
    print('------------------')

while True:
    print('(-1): VOTO EM BRANCO | (VALOR INEXISTENTE): VOTO ANULADO')
    x = int(input('INSIRA O NUMERO DO CANDIDATO DESEJADO: '))
    if x == -1:
        print('VOTO EM BRANCO')
        blank_votes += 1
    elif x not in vote.keys():
        print('VOTO ANULADO')
    else:
        for number_candidate, vote_candidate  in vote.items():
            if x == number_candidate:
                print(f'CANDIDATO VOTADO {vote_candidate[0]}')
                vote_candidate[1] += 1
    choice = input('TERMINOU DE VOTAR: (S OU N) ')
    if choice == 'S':
        break

for name_candidate, vote_candidate in vote.values():
    print('-'*10)
    print(f'CANDIDATO: {name_candidate}')
    print('-'*10)
    print(f'QUANTIDADE DE VOTOS: {vote_candidate}')
    print('-'*10)
print(f'VOTOS EM BRANCO: {blank_votes}')
x = []
for vote_candidate in vote.values():
    x.append(vote_candidate[1])

z = max(x)
for keys in vote.values():
    if z == keys[1]:
        y = keys[0]
        break
print(f'O GANHADOR DAS ELEIÇÕES DE 2022 FOI: {y}')
    
            
    
    
    
