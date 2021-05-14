'''Desafio 1 - Escreva um programa que determine todos os números de 4
algarismos que possam ser separados em dois números de dois algarismos que
somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
Exemplo: 3025 = 55 e 55**2 é igual á 3025'''

from random import randint

for i in range(0,10000):
    aux = str(randint(1000,10000))#gera um número aleatório 
    aux2 = int(aux[:2])
    aux3 = int(aux[2:])
    if (aux2 + aux3)**2 == int(aux):
        print(f'o número {aux} cortado ao meio e somado {aux2} + {aux3} elevados ao quadrado tem o mesmo valor {(aux2 + aux3)**2}')

    