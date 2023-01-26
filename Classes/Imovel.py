class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def calcular_preco(self):
         self.preco += self.adicional
         return self.preco


class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto
    
    def calcular_preco(self):
        self.preco -= self.desconto
        return self.preco

imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

print(imovel.endereco)                                      
print('Preço:', imovel.preco)                               

print(imovel_novo.endereco)                                 
print('Preço:', imovel_novo.preco)                          
print('Preço Atualizado:', imovel_novo.calcular_preco())    

print(imovel_velho.endereco)                                
print('Preço:', imovel_velho.preco)                         
print('Preço Atualizado:', imovel_velho.calcular_preco())

