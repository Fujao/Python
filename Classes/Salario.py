class Funcionario:
    def __init__(self, nome, sobrenome, salario_mensal, aumentar, anual):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal
        self.aumentar = aumentar
        self.anual = anual
        

    def aumentar_salario(self):
        if self.salario_mensal > 0:
            self.aumentar = self.salario_mensal * 1.10
            print(f'Salario com aumento: {self.aumentar}')
        else:
            print('Erro salario negativo')

    def salario_anual(self):
        if self.salario_mensal > 0:
            self.anual = self.salario_mensal * 12
            print(f'Salario com aumento: {self.anual}')
        else:
            print('Erro salario negativo')
    
    def exibe(self):
        print(f'Nome do funcionario: {self.nome}')
        print(f'Nome do funcionario: {self.sobrenome}')
        print(f'Salario mensal: {self.salario_mensal}')


funcionario1 = Funcionario('Marcos', 'Almeida', 150.00, 0, 0)
funcionario2 = Funcionario('Camila', 'Anchieta', 2000.00, 0, 0)

funcionario1.exibe()
funcionario2.exibe()

funcionario1.aumentar_salario()
funcionario2.aumentar_salario()

funcionario1.salario_anual()
funcionario2.salario_anual()
