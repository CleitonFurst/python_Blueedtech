#01 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha:
from time import sleep
senha = ''

while senha != '123':
    valida = input('Digite a senha :')
    if valida == '123':
        senha = '123'
        print('Carregando ...')
        sleep(3)
        print('Seja bem vindo!!!')
    else:
        print('Digitou a sneha errada !!!! \nDigite a senha novamente !!!')

