from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '15/12/2003', 1200.00)
    print(f'Teste = {funcionario_teste.idade()}')
    
    funcionario_teste1 = Funcionario('Teste', '15/12/1997', 1200.00)
    print(f'Teste = {funcionario_teste1.idade()}')
    

teste_idade() 

funcionario_teste = Funcionario('Arthur Teles Coutinho', '15/12/2003', 1200.00)
print(funcionario_teste.sobrenome())
