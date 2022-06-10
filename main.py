__Author__ = "Breno Escobar"

from Funções import hello
hello()
#CHAMANDO A FUNÇÃO NO "MAIN.PY"
#-------------------------------------------------------#
#PARÂMETROS E ARGUMENTOS
print('-' * 50)
from Funções import maior
maior(4,7)
#-------------------------------------------------------#
#ESCOPO DAS VARIÁVEIS
print('-' * 50)
from Funções import soma
#variável local recebendo valor -> total = 10
total = 10
#chamada do módulo soma de Funções usando sua variável
soma(3,5)
#impressão da variável local do programa principal
print("Total principal = ",total)
#-------------------------------------------------------#
#RETORNO DE VALORES
print('-' * 50)
import Funções
s = Funções.soma3(3,5)
print("Soma = ",s)
#-------------------------------------------------------#
#VALOR PADRÃO
print('-' * 50)
j = Funções.calcula_juros(500,20)
print("O juros é = ", j)
#-------------------------------------------------------#
#FUNÇÃO PARA DESENHA LINHA
#FUNÇÃO QUE RECEBA COMO PARÂMETRO UMA LISTA
print('-' * 50)
print("Resposta do Exercício 01\n")
from Ex_Funções import linha
linha(50)
print("\nResposta do Exercício 02\n")
from Ex_Funções import imprime_lista
L = [3,6,8,9,10,9,8,4]
imprime_lista(L)
print("\n\n")
#-------------------------------------------------------#
'''import Estrutura_de_decisão
print(Estrutura_de_decisão)

import Ex_Estru_decisão
print(Ex_Estru_decisão)

import Estrutura_de_repetição
print(Estrutura_de_repetição)

import Ex_Estru_repetição
print(Ex_Estru_repetição)'''