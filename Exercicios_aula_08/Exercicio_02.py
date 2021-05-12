
#02 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
# conte quantas vezes aparece as vogais a,e,i,o,u.

frase  = input('Digite uma frase:').lower()
a = 0
e = 0
i = 0 
o = 0
u = 0
for letra in frase:
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra =='o':
        o += 1
    elif letra == 'u':
        u += 1
    else:
        continue
print(f'Tem {a} vogais a ')
print(f'Tem {e} vogais e ')
print(f'Tem {i} vogais i ')
print(f'Tem {o} vogais o ')
print(f'Tem {u} vogais u ')




    
