def cria_matriz(L, C):
    M = []
    linha = C * [0]
    for i in range(L):
        M.append(linha[:])    
    return M


def exibe_matriz(M, L, C):
    for i in range(L):
        print('| ', end='')
        for j in range(C):
            print(M[i][j], end=' ')
        print('|')

def preenche_matriz(M, L, C):
    for i in range(L):
        for j in range(C):
            M[i][j] = float(input(f'M[{i}][{j}] = '))
        print()
    
    
alunos = cria_matriz(10, 3)
exibe_matriz(alunos, 10, 3)
