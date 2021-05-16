'''4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário 
é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha 
mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.'''


def salario(horas,vl_hora):

    if horas > 40:
        hora_extra = (horas - 40) * 1.5        
        soma_horas = hora_extra + horas
        result = soma_horas * vl_hora
        return result
    else:
        result = horas * vl_hora
        return result

        
nome = input('Digite o nome do funcionário: ')
horas = float(input(f'Digite a quantidade de horas trabalhadas do {nome}: '))
valorHora = float(input(f'Digite o valor da hora trabalhada do {nome}: '))
sal = salario(horas,valorHora)
print(f'O salário do funcionário {nome} é R${sal}')