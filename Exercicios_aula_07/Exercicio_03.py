'''3. Faça um programa com uma função chamada somaImposto. A função possui dois 
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em 
porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o 
valor de custo para incluir o imposto sobre vendas'''


def somaImposto(taxaImposto,custo):

    percentual =  taxaImposto/100
    valor_imposto = percentual * custo
   
    return valor_imposto


def altera(valor, valor_imposto):
    result = valor + valor_imposto
    return result


valor = float(input('Digite o valor do produto :'))
taxa = float(input('Digite o a taxa de imposto sobre o valor :'))

valor_imposto = somaImposto(taxa, valor)
novo_valor = altera(valor, valor_imposto)


print(f'O produto com o valor R${valor} com {taxa}% de imposto vai ficar {novo_valor}')

