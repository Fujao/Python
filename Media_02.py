dic = {}

for i in range(5):
    ra = input()
    n1, n2, n3 = input().split()
    n1, n2, n3 = float(n1), float(n2), float(n3) 
    dic[ra] = [n1, n2, n3]


for ra, notas in dic.items():
    media = sum(notas) / len(notas)
    print(ra)
    print(media)
