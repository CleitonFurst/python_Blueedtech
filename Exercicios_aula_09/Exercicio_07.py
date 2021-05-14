'''5. Faça um programa que mostre os valores numéricos inteiros ímpares situados
na faixa de 0 a 20.'''

lista = list(range(0,21))
lista2 = list()
for i in lista:
    if i % 2 != 0:
        lista2.append(i)
    
print(f'Os númeors impares dentro do intervalo de 0 a 20 são {lista2}')


