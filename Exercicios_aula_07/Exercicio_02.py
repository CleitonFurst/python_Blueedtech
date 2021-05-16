'''Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e
retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''

from random import randint


def parametros(a, b):
    limite = randint(0, 100)
    print(f'O limite escolhido pela maquina foi {limite}')
    soma = a + b
    if limite == 100:
        limite -= 5
    elif soma > limite:
        return True
    else:
        return False


print('Tente digitar dois números de 0 a 50 que sau soma seja maior que o limite que a maquina irá escolher')
while True:
    a = int(input('Digite o primeiro valor :'))
    b = int(input('Digite o segundo valor :'))
    resposta = parametros(a,b)
    if resposta == True:
        print(f'Você digitou {a} e {b} e a soma dos dois é {a + b} que é maior que o limite escolhido pela maquina.\n Parabens !!!')
        break
    else:
        print(f'Você digitou {a} e {b} e a soma dos dois é {a + b} que é menor que o limite escolhido pela maquina')
        print('Tente novamente !!!')