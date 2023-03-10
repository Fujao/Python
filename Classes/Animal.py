class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas
    
    def exibir_dados(self):
        print('Nome: ', self.nome)
        print('Cor: ', self.cor)
        print('Numero de patas', self.numero_patas)

class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca

    def exibir_dados(self):
        print('Nome: ', self.nome)
        print('Cor: ', self.cor)
        print('Numero de patas', self.numero_patas)
        print('Raca: ', self.raca)


animal = Animal("Passarinho", "Azul", 3)
animal.exibir_dados()       

dog = Cachorro("Rex", "Marrom", 3, "Vira lata")
dog.exibir_dados()
