'''
4.	Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 
Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogaodor1': randint(1,6),
    'jogador2' : randint(1,6),
    'jogador3' : randint(1,6),
    'jogador4' : randint(1,6)
}
print('Valores que os jogadores sortearam ...')
for g , v in jogadores.items():
    print(f'{g} conseguiu tirar {v}')
    sleep(0.5)
ranking = dict()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('vencedores')
for i , j in enumerate(ranking):
    print(f'{i + 1}º {j}')
    