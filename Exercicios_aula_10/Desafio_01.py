
'''#DESAFIO:

Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 

Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;'''

candi1 = 0
candi2 = 0
candi3 = 0
candi4 = 0
nulos = 0
branco = 0
x = 1 
while x != 0:    
    op = int(input('*************QUAL SERÁ SEU VOTO*********************\n'
                                '1 -> Jose  \n'                      
                                '2 -> João \n'
                                '3 -> Marina \n'
                                '4 -> Lula \n'
                                '5 -> Nulo \n'
                                '6 -> Em Branco \n'
                                '0 -> Sair\n'                       
                                'Escolher :'))

    if op == 1:
         candi1 += 1
    elif op == 2:
         candi2 += 1
    elif op == 3:
         candi3 += 1
    elif op == 4:
         candi4 += 1
    elif op == 5:
         nulos += 1
    elif op == 6:
         branco += 1
    else:
        x = 0
         
print(f'****Distribuição dos votos !!*****')
print(f'Total de votos no candidato Jose -> {candi1}')
print(f'Total de votos no candidato João -> {candi2}')
print(f'Total de votos no candidata Marina -> {candi3}')
print(f'Total de votos no candidato Lula -> {candi4}')
print(f'Total de votos Nulos -> {nulos}')
print(f'Total de votos Em Branco -> {branco}')

