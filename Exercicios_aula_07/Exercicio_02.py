'''2. Faça um programa, com uma função que necessite de um argumento. A função retorna 
o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for 
negativo e ‘0’ se for 0'''

def numero(n):
    if n > 0:
        return 'P'
    elif n < 0:
        return 'N' 
    else:
        return 0


num = int(input('Digite um número (Negativo ou Positivo):'))

valor = numero(num)

if valor == 'P':
    result = 'Positivo'
elif valor == 'N':
    result = 'Negativo'
else:
    result = str(0)


print(f'O número {num} é {result}')
