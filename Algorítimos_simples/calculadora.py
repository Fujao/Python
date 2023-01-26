calcular = input('Calcular (s/n)? ')
while calcular == 's':
    x = float(input('x: '))
    op = input('operador: ')
    y = float(input('y: '))
    if op == '+':
        resultado = x + y
    elif op == '-':
        resultado = x - y
    elif op == '*':
        resultado = x * y
    elif op == '/':
        if y == 0:
            print('Divisão por zero!/n')
            break
        else:
            resultado = x / y
    print(f'{x} {op} {y} = {resultado}/n')
    calcular = input('Calcular (s/n)? ')
print('Calculadora encerrada')
              
        
    
