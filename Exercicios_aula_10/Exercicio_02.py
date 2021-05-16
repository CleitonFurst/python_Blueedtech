#02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

resposta = str(input('Digite o seu sexo (M/F)')).upper()
while resposta not in 'MF' :
    resposta = str(input('Digite o seu sexo (M/F)')).upper()
print(f'Sexo {resposta} registrado !!')