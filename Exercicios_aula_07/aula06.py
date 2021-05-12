'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno:
'''


def area(dim1 = 0 , dim2 = 0):

    area = dim1 * dim2
    print(f'O terreno tem a área de largura {dim1} X {dim2} é de {area} m² ')


valor1 = float(input('Digite o comprimento do terrno (m²) :'))
valor2 = float(input('Digite a largura do terreno (m²) :'))

area(valor1,valor2)



