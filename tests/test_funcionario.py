from codigo.bytebank import Funcionario


class TestFuncionario:
    def test_quando_idade_recebe_01_01_2001_deve_retornar_ano_atual_menos_2001(self):
        entrada_dada = '01/01/2001'
        saida_esperada = 22
        
        funcionario = Funcionario('Teste', entrada_dada, 1111)
        resultado_obtido = funcionario.idade()
        
        assert resultado_obtido == saida_esperada
        
    def test_quando_sobrenome_recebe_Lucas_Nobre_deve_retornar_Nobre(self):
        entrada_dada = 'Lucas Nobre'
        saida_esperada = 'Nobre'
        
        lucas = Funcionario(entrada_dada, '11/11/2001', 1111)
        resultado_obtido = lucas.sobrenome()
        
        assert resultado_obtido == saida_esperada
