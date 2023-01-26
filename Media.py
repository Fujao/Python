A,B,C,D = map(float,input().split())
M = (A*2+B*3+C*4+D*1)/10
print(f'Media: {M:.1f}')
if M>=7.0:
    print("Aluno aprovado.")
elif M<5.0:
    print("Aluno reprovado.")
elif 5.0<= M <=6.9:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (M+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')
    



