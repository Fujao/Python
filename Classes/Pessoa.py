class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome
    
class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj
    

class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf


pessoa1 = Pessoa(1, "Marcos")
p_juridica = PessoaJuridica(2, "Carlos", "1111111111")
p_fisica = PessoaFisica(3, "Maria", "222222222", "333333333")


print(pessoa1.identificador)        
print(pessoa1.nome)                 

print(p_juridica.identificador)     
print(p_juridica.nome)              
print(p_juridica.cnpj)              

print(p_fisica.identificador)       
print(p_fisica.nome)                
print(p_fisica.rg)                  
print(p_fisica.cpf)

