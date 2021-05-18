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

while True:
    dados.append(str(input('Digite o nome da pessoa :')))
    dados.append(int(input('Digite a peso da pessoa :')))
    pessoas.append(dados[:])
    dados.clear()
    
    op = str(input('Deseja continuar ?(S/N):').strip().upper())
    if op == 'N':
        break
    elif op == 'S':
        continue
    else:
        print('Digite apena S ou N !!!')
        break
maior = max(pessoas)
menor = min(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas e a pessoa com maior peso é o(a) {maior[0]} com {maior[1]}Kg e a pessoa com o menor peso é o(a) {menor[0]} com {menor[1]}Kg')
    