import pytest

from codigo.bytebank import Funcionario
from pytest import mark


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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_dada = 100000
        saida_esperada = 90000

        funcionario_diretor = Funcionario(
            'Paulo Bragança', '11/11/2000', entrada_dada)
        funcionario_diretor.decrescimo_salario()

        resultado_obtido = funcionario_diretor.salario

        assert resultado_obtido == saida_esperada
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_dada = 1000
        saida_esperada = 100
        
        funcionario = Funcionario('Teste', '11/11/2000', entrada_dada)
        resultado_obtido = funcionario.calcular_bonus()
        
        assert resultado_obtido == saida_esperada
        
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_dada = 1000000
            
            funcionario = Funcionario('Teste', '11/11/2000', entrada_dada)
            resultado_obtido = funcionario.calcular_bonus()
            
            assert resultado_obtido
            