# 03 -Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10.
#  O jogador vai tentar adivinhar qual número foi escolhido até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0,10)
num2 = None
cont = 0
while num != num2:
    resposta = int(input('Digite o valor que você acha que o computaodor sorteou :'))
    num2 = resposta
    cont += 1
if cont == 1:
    print(f'Computador sorteou o número {num} e você acertou de primeira parabéns !!')   
else:
    print(f'Computador sorteou o número {num} e você tentou adivinhar {cont} vezes !!')   
