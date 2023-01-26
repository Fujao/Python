class Carro:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print('-' * 20)
        print(f'Marca do carro: {self.marca}')
        print(f'Modelo do carro: {self.modelo}')
        print(f'Placa do carro: {self.placa}')
        print('-' * 20)


carro1 = Carro('Mercedes benz', 'AMG GT', 'BGH390')
carro2 = Carro('Audi', 'RS6', 'UOE009')

carro1.exibir_dados()
carro2.exibir_dados()




