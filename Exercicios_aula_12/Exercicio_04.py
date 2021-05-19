#04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista 
# composta.
from random import randint


sorteados = list()

num = int(input('Quantos jogod ira fazer :'))   

def palpites():
    palpites = list()
    for i in range(0,6):
        num1 = randint(1,60)
        if num1 not in sorteados:
            palpites.append(num1)
    return palpites
            
for i in range(0,num):     
    sorteados.append(palpites())
    print(f'{i + 1} -> {sorteados[i]}')
   


               

   
    
    
    
    