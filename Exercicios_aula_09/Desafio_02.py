'''Desafio 2 - Faça um script que peça ao usuário o número de matérias da escola,
ou seja, um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, de
cada matéria e isso será armazenado numa lista. Ao final, seu script deverá
fornecer a média geral do aluno.'''

num = int(input('Digite o número de matérias :'))
lista = []
media = 0.0
for i in range(0,num):
    nota = float(input('Digite a nota da matéria :'))
    lista.append(nota)
    media  = (media + lista[i])
print(f'A média geral do aluno das {len(lista)} matérias com as notas {lista} será igual a {media/num}')

