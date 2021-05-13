
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
a  = 0 
for i in tupla:
    if i == 9:
        soma += 1
    elif i == 3 and a == 0 :
        index = tupla.index(3)
        a += 1
    else:
        continue

print(f'O número 9 aparece {soma}')
print(f'O primeiro 3 foi digitado na posição {index}')