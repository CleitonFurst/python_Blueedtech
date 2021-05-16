'''Exercício 6
Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as
duas notas mais altas para calcular a média.
Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3
provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.'''

def media_final(n1,n2,n3):
    if n1 > n3 and n2 > n3 :
        media = (n1 + n2) / 2
        nota1 = n1 
        nota2 = n2        
    elif n2 > n1 and n3 > n1 :
        media = (n2 + n3) / 2    
        nota1 = n2 
        nota2 = n3    
    elif n1 > n2 and n3 > n2:
        media = (n1 + n3) / 2  
        nota1 = n1 
        nota2 = n3      
    else:
        media = (n1 + n2) / 2
        nota1 = n1
        nota2 = n2
    media_geral = (n1 + n2 +n3) / 3
    nota_mais_alta = max(n1, n2, n3)
    nota_mais_baixa = min(n1, n2, n3)
    print(f'As suas notas no semestre foram {n1 , n2, n3}\nForam consideradas apenas as duas maiores notas {nota1} e {nota2}\nSua média ficou {media:.2f} ')
    print(f'A sua nota mais alta foi {nota_mais_alta}')
    print(f'A sua menor nota foi {nota_mais_baixa}')
    print(f'A sua média se fosse considerado as tres notas ficaria {media_geral:.2f}')
    if media <= 7 :
        print(f'Média {media} menor que 7 você Reprovou !!!')
    
n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
n3 = float(input('Digite a terceira nota :'))

media_final(n1,n2,n3)