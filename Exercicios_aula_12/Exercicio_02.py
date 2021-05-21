#02 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:
""" 
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
"""

matriz = [[0, 0, 0], [0, 0, 0],[0, 0, 0]]

for i in range(0, 3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite um número [{i},{j}]:'))

for i in range(0,3):
    for j in range(0,3):
        print(f'[\t{matriz[i][j]}\t]',end =' ' )
    print()
