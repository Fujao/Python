valor = input().split(" ")

a,b,c=valor
pi = 3.14159

triangulo = (float(a)*float(c)/2)
circulo = pi*(float(c)*float(c))
trapezio = float(c)*(float(b)+float(a))/2
quadrado = (float(b)*float(b))
retangulo = (float(a)*float(b))

print(f'TRIANGULO: {triangulo:.3f}\n CIRCULO: {circulo:.3f}\n TRAPEZIO: {trapezio:.3f}\n QUADRADO: {quadrado:.3f}\n RETANGULO: {retangulo:.3f}')
