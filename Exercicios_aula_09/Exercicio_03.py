'''1. Crie um código em Python que pede qual tabuada o usuário quer ver, em
seguida imprima essa tabuada.'''


num = int(input('Digite o número de qual tabuada o usuário quer ver :'))
tabuada = list
multip = 0
for i in range(1,11):
    multip = i * num
    print(f'{i} X {num} = {multip}')