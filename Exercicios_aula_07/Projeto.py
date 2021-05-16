'''PROJETO: Gastos com viagem - Escrever uma aplicação utilizando funções que calcule os
gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma
determinada cidade.
Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado
'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.
Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da
passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.
Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.
Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade
de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!
Gastos Extras
5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e
some esse valor ao total da viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00'
adicionais.'''


def custo_hotel(noites):
    valor = noites * 140
    return valor


def custo_aviao(cidade):
    if cidade == 1:
        return 312.00
    elif cidade == 2:
        return 447.00
    elif cidade == 3:
        return 831.00
    else:
        return 986.00


def custo_carro(dias):
    if dias < 3:
        valor = dias * 40
        return valor
    elif dias >=3 and dias < 7:
        valor = (dias * 40) - 20
        return valor
    else:
        valor = (dias * 40) - 50
        return valor
    

def valor_viagem(cidade, dias, gastos_extras = 0):
    valor1 = custo_aviao(cidade)
    valor2 = custo_carro(dias)
    valor3 = custo_hotel(dias - 1)
    soma = valor1 + valor2 + valor3 + gastos_extras
    return soma


while True:
    op = int(input('****Para qual cidade deseja viajar ?*****\n'
                    '1-> São Paulo custa R$ 312,00\n'
                    '2-> Porto Alegre custa R$ 447,00\n'
                    '3-> Recife custa R$ 831,00\n'
                    '4-> Manaus custa R$ 986,00\n'
                    '5-> Sair\n'
                    'Escolha:'))
    if op == 1:
        cidade = 1
        break
    elif op == 2:
        cidade = 2
        break
    elif op == 3:
        cidade = 3
        break
    elif op == 4:
        cidade = 4
        break
    else:
        break

dias = int(input('Quantos dias de viagem :'))
extras = float(input('Gastou extras da viagem :'))
valor = valor_viagem(cidade,dias,extras)
print(f'O custo total da viagem fica R${valor:.2f}')


