'''Crie um programa que leia a idade e o sexo de várias pessoas. A
cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''


cont1 = 0
cont2 = 0
cont3 = 0
while True:
    idade = int(input('Digite a idade da pessoa :'))
    sexo = str(input('Digite o sexo da pessoa use apenas (M/F):')).upper()    
    saida = input('Desaca continuar (S/N):').upper()    
    if sexo == 'M':
        cont2 += 1
        
    if idade > 18:
        cont1 += 1
        
    if idade < 20 and sexo == 'F':
        cont3 += 1
        
    if saida != 'S':
        break

    
print(f'Faram cadastradas {cont1} pessoas maiores de 18 anos\nForam cadastrados {cont2} homens\nForam cadastradas {cont3} munlheres com idade menor que 20 anos ')