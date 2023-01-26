def muda_total(l):
   for i in range(len(l)):
       l[i] = int(l[i])

def show(price):
   for i in range(len(price)):
       if i < len(price) -1:
           print(price[i], end=' ')
       else:
           print(price[i])
price = input().split()
if price != []:
   muda_total(price)
x = input().split()
while x[0] != 'encerrar':
   if x[0] == 'adicionar':
       price.append(int(x[1]))
   elif x [0] == 'remover':
       x[1]=int(x[1])
       if x[1] in price:
            price.remove(x[1])
       else:
            print(f'código {x[1]} não encontrado')
   else:
       price.sort()        
       show(price)  
   x = input().split()  
price.sort()        
show(price)
