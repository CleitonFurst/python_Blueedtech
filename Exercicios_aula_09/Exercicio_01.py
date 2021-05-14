'''#01 - Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
a) tamanho da lista.
b) maior valor da lista.
c) menor valor da lista.
d) soma de todos os elementos da lista.
e) lista em ordem crescente.
f) lista em ordem decrescente.
'''


L = [5, 7, 2, 9, 4, 1, 3]
tamanho = len(L)
maior = max(L)
menor = min(L)
soma = sum(L)
ordenada = L.sort()
L.sort()
print(L)
L.reverse()
print(L)
print(f'{tamanho}')
print(f'{maior}')
print(f'{menor}')
print(f'{soma}')
