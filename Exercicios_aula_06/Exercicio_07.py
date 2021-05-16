'''7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
forem iguais, imprima que eles são iguais.'''

def menor_valor(val_1, val_2):
    if val_1 < val_2:
        print(f'O menor valor entre {val_1} e {val_2} é o {val_1}')
    elif val_1 > val_2:
        print(f'O menor valor entre {val_1} e {val_2} é o {val_2}')
    elif val_1 == val_2:
        print(f'Os valores {val_1} e {val_2} são iguais !!')
    else:
        print('Só aceita valores númericos para a comparação !!!')


num1 = float(input('Digite o primeiro valor :'))
num2 = float(input('Digite o segundo valor :'))

menor_valor(num1,num2)