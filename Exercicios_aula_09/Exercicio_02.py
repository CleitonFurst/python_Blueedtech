'''#02 - Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''



lista = ['Telefonou para a vítima?(sim/Não) :','Esteve no local do crime?(sim/Não) :','Mora perto da vítima?(sim/Não) :','Devia para a vítima?(sim/Não) :','Já trabalhou com a vítima?(sim/Não) :' ]
print('Responda Sim ou Não para as perguntas perguntas a seguir ')
sim = 0
nao = 0
while True:
    cont = len(lista)
    for i in lista:
        if cont == 0:
            break
        resposta = input(f'{i}').upper()
        if resposta == 'SIM':
            sim += 1
        elif resposta == 'NÃO' or resposta == 'NAO':
            nao += 1
        elif resposta != 'SIM' or resposta != 'NÃO' :
            break
        else:
            print(f'A resposta {resposta} é invalida !!!')
            break
        cont -= 1
    if sim == 2:
        print('Pessoa classifica como suspeita !!!')
    elif sim == 3 or sim == 4:
        print('Pessoa classificada como Cúmplice !!! ')
    elif sim == 5:
        print('Pessoa classificada como Assassino !!! ')
    else:
        if resposta == 'SIM' or resposta == 'NÂO' or resposta == 'NAO':    
            print('Pessoa classificada como Inocente !!!')
    break
    
