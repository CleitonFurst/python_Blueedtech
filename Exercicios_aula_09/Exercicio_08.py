'''6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o
exemplo abaixo:
preço do pão: R$ 0,18
panificadora pão de ontem - tabela de preços 
1 -R$ 0,18
2 - R$ 0,36
50 -R$ 9,00
'''
lista = list(range(1,51))

preco = float(input('Digite o preço do pão por unidade R$ '))

for i in lista:
    print(f'{i} -> R${(i*preco):.2f} ')
