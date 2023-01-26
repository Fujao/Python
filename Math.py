import math
x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())

distancia = math.sqrt((float(x2) - float(x1))*(float(x2) - float(x1)) + (float(y2) - float(y1))*(float(y2) - float(y1)))

print('%0.4f'%distancia)