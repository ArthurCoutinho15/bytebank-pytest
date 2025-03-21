from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass():
    
    def test_quando_idade_recebe_15_12_2003_deve_retornar_22(self):

        entrada = '15/12/2003' # Given-Contexto
        esperado = 22
        
        funcionario_teste = Funcionario('Teste', entrada, 1200.00)

        resultado = funcionario_teste.idade() # When-Ação
        
        assert resultado == esperado # Then-Desfecho
    
    def test_quando_nome_recebe_neymar_santos_silva_deve_retornar_silva(self):
        entrada = 'Neymar Santos Silva'
        esperado = 'Silva' 
        
        funcionario_teste = Funcionario(entrada, '15/12/2003', 1200.00)
        
        resultado = funcionario_teste.sobrenome()
        
        assert resultado == esperado
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        
        resultado = funcionario_teste.descrescimo_salario() #When
        
        assert resultado == esperado # Then
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #Given
        esperado = 100
        
        funcionario_teste = Funcionario('Ana', '14/12/2004', entrada)
        
        resultado = funcionario_teste.calcular_bonus() #When
        
        assert resultado == esperado  #Then
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception): 
            entrada = 1000000 #Given
            
            funcionario_teste = Funcionario('Ana', '14/12/2004', entrada)
            
            resultado = funcionario_teste.calcular_bonus() #When
            
            assert resultado  #Then
    