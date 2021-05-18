# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista, 
# depois do dado inserido,
# pergunte ao usuário se ele quer continuar, 
# se ele não quiser pare o programa.
# No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso

pessoas = list()
dados = list()
maior = 0
menor = 0
while True:
    dados.append(str(input('Digite o nome da pessoa :')))
    dados.append(float(input('Digite a peso da pessoa :').replace(',','.')))
    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    
    op = str(input('Deseja continuar ?(S/N):').strip().upper())[0]
    if op == 'N':
        break
    elif op == 'S':
        continue
    else:
        print('Digite apena S ou N !!!')
        break

print(f'Foram cadastradas {len(pessoas)}  maior peso é  {maior}Kg e o menor peso é  {menor}Kg')
    