
#03 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores.

num = int(input('digite um número inteiro :'))

for i in range(1,num + 1):    
    if num % i == 0:
        print(f'{i} é um divisor de {num}')
