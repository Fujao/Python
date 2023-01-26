class ContaBancaria:
    def __init__(self, numero, titular, senha, saldo, variavel, variavel2):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.variavel = variavel
        self.variavel2 = variavel2

    def password(self, valor, senha):
        if self.senha == senha:
            self.variavel = self.saldo + valor
            print(f'Saldo pos deposito: R${self.variavel}')
        else:
            print('Senha incorreta')



    def sacar(self, valor, senha):
        if self.senha == senha:
            self.variavel2 = self.variavel - valor
            print(f'Saldo pos saque: R${self.variavel2}')
        else:
            print('Senha incorreta')

    
    def exibe(self):
        print(f'Titular da conta: {self.titular}')
        print(f'Numero da conta: {self.numero}')
        print(f'Saldo inicial: {self.saldo}')


conta1 = ContaBancaria(999, 'Paulo Roberto', 1234, 0, 0, 0)


conta1.exibe()
conta1.password(2000.00, 1234)
conta1.sacar(1000.00, 1234)


