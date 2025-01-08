#Sistema de Cadastro de Funcionários

class Funcionario:
    def_init_(self, nome: str, idade: int, cargo: str):
    self.nome = nome 
    self.idade = idade
    self.cargo = cargo

    def_str_(self):
    return f"Nome: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}"
