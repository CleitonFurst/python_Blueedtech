#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]

for i in range(0, 3):
    for j in range(0,3):
        matriz[i][j] = int(input('Digite um número:'))
        
soma = 0
soma_c3 = 0
cont = 0
aux = list()
maior = 0 
for i in range(0,3):
    for j in range(0,3):
      cont += 1
      if cont > 6:
         soma_c3 += matriz[i][j]
      if cont > 3 and cont < 6:
         aux.append(matriz[i][j])
         maior = max(aux)
      soma += matriz[i][j]
      print(f'[ {matriz[i][j]} ]',end =' ' )
    print(' ')

print(f'A soma de todos os elemntos da matriz é igual á {soma}')
print(f'A soma dos valores da terceira coluna é igual a {soma_c3}')
print(f'O maior valor da segunda linha {maior}')
