#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.


cont_m18 = 0
cont_h = 0
cont_M20 = 0
while True:
    idade = int(input('Digite a idade da pessoa :'))
    sexo = str(input('Digite o sexo da pessoa :').strip().upper()[0])
    if idade > 18:
        cont_m18 += 1
    if sexo == 'M':
        cont_h += 1
    if sexo == 'F' and idade < 20:
        cont_M20 += 1
    op = input('Deseja sair (S/N):').strip().upper()[0]
    if op == 'N':
        break

print(f'{cont_m18} pessoas tem mais de 18 anos !!')
print(f'{cont_h} homens foram cadastrados !!')
print(f'{cont_M20} mulhere(s) com menos de 20 anos foram cadastradas !!!')
