'''Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o
menor dos dois. Se eles forem iguais, imprima que são valores idênticos.'''


def verefica_valor(valor1, valor2):
    if valor1 == valor2:
        print('Valores identicos !!')
    else:
        print(f'O menor valor é {max(valor1,valor2)}')
    

valor1 = int(input('Digite o priemiro valor :'))
valor2 = int(input('Digite o segundo valor :'))

verefica_valor(valor1, valor2)
