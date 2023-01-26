class ContaBancaria:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Deposito realizado. saldo: R$ {self.__saldo}')

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f'Saque falhou. Saldo: R$ {self.__saldo}')
            return 'Saldo insuficiente'
        self.__saldo -= valor
        print(f'Saque realizado. Saldo: R$ {self.__saldo}')
        return valor


    
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)
        self.rendimento = 0.5

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, titular, gerente):
        super().__init__(numero, titular)
        self.gerente = gerente

    def sacar(self, valor):
        print('Verificando prazo do investimento....')
        print('calculando impostos e taxas')
        print('realizando saque...')
        return super().sacar(valor)
            

