'''
3.	Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. 
Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
'''
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno :'))
aluno['media'] = float(input('Digite a média do aluno :'))
if aluno.get('media') >= 7:
    aluno['situacao'] = 'Aprovado'
elif  5 <= aluno.get('media') <= 7:
    aluno['situacao'] = 'Em recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'A média do aluno {aluno["nome"]} foi {aluno["media"]} o aluno esta {aluno["situacao"]}')