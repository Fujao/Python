class funcionario:
    def __init__(self):
        self.nome = input('Nome do funcionario:')
        self.salario = float(input('Salario do funcionario:'))
        self.aumento = float(input('Informe a porcentagem de aumento:'))
        print(f'Nome: {self.nome} e salario: {self.salario}')
        print(f'Nome: {self.nome} e Salario com aumento: {(self.salario * self.aumento)+self.salario}')

informacoes = funcionario()
