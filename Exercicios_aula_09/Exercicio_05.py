'''3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e
mostre ao final a quantidade de pessoas de cada estado civil.
'''

estado = list('')
solteiro = 0
casado = 0

for i in range(1,16):    
    resp = input(f'Digite o estado sivil da {i}ª pessoa:').upper().strip()
    if resp == 'SOLTEIRO':
        solteiro += 1
    elif resp == 'CASADO':
        casado += 1
    else:
        print('Resposta invalida!!!')
        break
print(f'{solteiro} pessoas são solteiras e {casado} pessoas são casadas !!')
