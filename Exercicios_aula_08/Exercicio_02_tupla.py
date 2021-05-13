
#02 - Desenvolva um programa que leia quatro valores pelo 
# teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.

#B) Em que posição foi digitado o primeiro valor 3.

a = int(input('Digite o priemiro valor :'))
b = int(input('Digite o segudno valor :'))
c = int(input('Digite o terceiro valor :'))
d = int(input('Digite o quarto valor :'))

tupla = (a,b,c,d)
soma = 0
for i in tupla:
    if i == 3:
        soma += 1
    else:
        continue

index = tupla.index(3)
print(f'O número 9 aparece {soma}')
print(f'O primeiro 3 foi digitado na posição {index}')