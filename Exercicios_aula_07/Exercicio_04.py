'''Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse
exercício, pesquise sobre a função date da biblioteca Datetime.'''
from  datetime import date, datetime

def voto(data):
    atual = date.today()
    data_n = datetime.strptime(data,'%d/%m/%Y')
    idade = atual.year - data_n.year
    return idade
   
while True:    
    data = input('Digite a sua data de nacimento no formato (DD/MM/YYYY): ')
    if len(data) != len('DD/MM/YYYY'):
        print('Digite a data novamente formato invalido !!!')
    else:
        break

idade  = voto(data)
if idade >= 16 and idade <= 17:
    print(f'Você tem {idade} anos seu voto é Opcional !!! ')
elif idade > 17:
    print(f'Você tem {idade} anos seu voto é Obrigatório !!! ')
else:
    print(f'Você tem {idade} anos não tem idade para votar voto Negado!!! ')

    
    
    
    