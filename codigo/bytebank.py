from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        
        return nome_quebrado[-1]
    
    
    def _verifica_socios(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Coutinho', 'Yamato']
        
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
           
        
    def descrescimo_salario(self):
        if self._verifica_socios():
            novo_salario = self._salario * 0.9
            return novo_salario
    
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor
    

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'