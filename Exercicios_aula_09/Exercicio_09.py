'''8. Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
● #Dados:● #Cada palpite possui 6 dezenas
● #As dezenas variam de 1 até 60
● #Não pode repetir dezena
'''
from random import randint

lista = list()
for i in range(0,6):
    aux = randint(1,60)    
    if aux in lista:
        continue
    else:
        lista.append(aux)
print(f'As dezenas para a loteria são {lista}')
