# 01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)


def novos():
    valores = list()
    for i in range(2):
        valores.append(int(input(f'Digite o {i + 1}º valor :')))

    def soma(valores):
        soma = 0
        for i in valores:
            soma = valores[0] + valores[1]
        return soma

    def multiplicar(valores):
        mult = 0
        mult = (valores[0]) * (valores[1])
        return mult

    def maior(valores):
        if valores[0] > valores[1]:
            return valores[0]
        else:
            return valores[1]

    controle = 0
    while controle != 5:

        op = int(input('****MENU*****\n'
                       '1-> Soma\n'
                       '2-> multiplicar\n'
                       '3-> maior\n'
                       '4-> novos números\n'
                       '5-> sair do programa\n'
                       'Escolha:'))

        if op == 1:
            soma = soma(valores)
            print('-=-=' * 10)
            print(f'A soma dos valores é {soma}')
            print('-=-=' * 10)
        elif op == 2:
            mult = multiplicar(valores)
            print('-=-=' * 10)
            print(f'A multiplicaçaõ dos valores é {mult}')
            print('-=-=' * 10)
        elif op == 3:
            maior = maior(valores)
            print('-=-=' * 10)
            print(f'O maior dos valores é {maior}')
            print('-=-=' * 10)
        elif op == 4:
            novos()
        elif op == 5:
            controle = 5
        else:
            print('-=-=' * 10)
            print('Opção invalida !!!')
            print('-=-=' * 10)


novos()
