def channels(x):
   y = []
   for _ in range(x):
       n,i,m,p=input().split(';')
       i=int(i)
       m=float(m)
       p=p=='sim'
       y.append([n,i,m,p])
   return y 
def z(y, s_premium,s_n_premium):
   particao=[]
   for c in y:
       v=c[2]
       if c [3]:
           v += c[1] // 1000*s_premium
       else:
           v +=c[1] // 1000*s_n_premium
       particao.append([c[0], v])  
   return particao          
def show (particao):
   print('-----')
   print('BÔNUS')
   print('-----')
   for u in particao:
       print(f'{u[0]}: R$ {u[1]:.2f}')
x = int(input())
y = channels(x)
s_premium = float(input())
s_n_premium = float(input())  
particao = z(y,s_premium,s_n_premium)
show(particao)
