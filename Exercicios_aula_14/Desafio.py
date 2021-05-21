'''6.	DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
'''
dados = dict()
cadastros = list()
media = 0
soma = 0
mulheres = list()
acimamedia = list()
while True:
    print('Cadastro pessoas')
    dados['nome'] = str(input('Digite o nome :'))
    dados['sexo'] = str(input('Digite o sexo (M/F) :').strip().upper())
    dados['idade'] = int(input('Digite a idade :'))
    cadastros.append(dados.copy())
    op = str(input('deseja continual (S/N)').strip().upper()[0])
    if op == 'N': 
        break
    
for i in cadastros:
    soma += i['idade']
media = soma / len(cadastros)
print(media)
for i in cadastros:
    if i.get('sexo') == 'F': 
        mulheres.append(i['nome'])        
for i in cadastros:
    if i.get('idade') > media:
        acimamedia.append(i['idade'])
print(acimamedia)

