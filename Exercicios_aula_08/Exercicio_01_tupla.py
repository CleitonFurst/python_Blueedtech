#01 - Crie um programa que vai gerar cinco números aleatórios 
# de 1 a 50 e colocar em uma  tupla. Depois disso, mostre a listagem de 
# números gerados e também indique o menor e o maior valor que estão na tupla.
#  Sem utilizar repetições. Dica: 
# utilizar a biblioteca random do Python.


from random import randint
a = randint(1,50)
b = randint(1,50)
c = randint(1,50)
d = randint(1,50)
e = randint(1,50)

tupla = (a,b,c,d,e)
ordenada = sorted(tupla)
print(tupla)
print(f'O menor número da tupla é {ordenada[0]} e o maior número {ordenada[4]}')
    


