market = {"401": 120, 
          "402": 90, 
          "403": 95,
          "404": 105,
          "405": 115,
          "406": 99,
          "407": 60}



for key, values in market.items():
    print(f'Id = {key}, Value = {values}')



while True:
    x = int(input('Type value range to sniper: '))
    for key, value in market.items():
        if value <= x:
            print(f'Sniper sucess -------- {key}')
    y = input('You finished the sniper: Y / N: ')
    if y == 'Y':
        break
        

    







        





