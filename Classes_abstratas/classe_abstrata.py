from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def exibe_nome(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def exibe_nome(self):
        print("Nome do Funcionario: ", self.nome)

class Aluno(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
    
    def exibe_nome(self):
        print("Nome do Aluno: ", self.nome)


funcionario = Funcionario("Joao", 25, 1500.0)
aluno = Aluno("Pedro", 15, "Matematica")

funcionario.exibe_nome()
aluno.exibe_nome()
