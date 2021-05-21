'''5.	Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente ,além da idade , com quantos anos a pessoa vai se aposentar.
Considere que o trabalhador deve contribuir por 35 anos para se aposentar.'''

from datetime import datetime

dados = dict()
dados['nome'] = str(input('Digite o nome :'))
dados['anonac'] = int(input('Digite o ano de nacimento :'))
dados['carteira'] = int(input('Digite  o número da carteira de trabalho :'))
if dados.get('carteira') != 0:
    dados['anocont'] = int(input('Digite  o ano de contratação :'))
    dados['salario'] = float(input('Digite o salário :'))
ano = datetime.now()  
dados['idade'] =  int(ano.year) - dados.get('anonac') 
if dados.get('carteira') == 0:
    print(f'Se o(a) {dados["nome"]} começar a trabalhar este ano ainda vai levar 35 anos, ai vai se apposentar com {dados["idade"] + 35} anos')
else:
    trabalhados =  int(ano.year) - dados.get('anocont')
    print(trabalhados)
    print(f'Como o(a) {dados["nome"]} começou a trabalhar no ano de {dados["anocont"]}'
          ' e atualamente tem {dados["idade"]} vai se aposentar com {dados["idade"] + 35 - trabalhados} anos de idade com 35 anos de contribuição')