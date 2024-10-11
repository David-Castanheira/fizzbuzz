from src.fizzbuzz import fizzbuzz
import pytest 

# Função de teste que percorre a lista de entradas e saídas e verifica se os valores são iguais
# A fixture está definida no arquivo conftest.py
def test_fizzbuzz(casos_fizzbuzz):
    for entrada, saida_esperada in casos_fizzbuzz:
        assert fizzbuzz(entrada) == saida_esperada