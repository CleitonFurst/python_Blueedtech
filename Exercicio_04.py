'''4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário 
é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha 
mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.'''


def salario(horas,vl_hora):

    if horas > 40:
        hora_extra = horas - 40
        horas_calc = hora_extra * 1.5
        soma_horas = horas_calc + horas
        result = soma_horas * vl_hora


def salario(horas,valorHora):
    if horas > 40:
        extra = (horas - 40) * 1.5
        salarioBruto = (horas + extra) * valorHora
    else:
        salarioBruto = horas * valorHora

    return salarioBruto


nome = input("Digite o nome do funcionário: ")
horas = float(input(f"Digite a quantidade de horas trabalhadas do {nome}: "))
valorHora = float(input(f"Digite o valor da hora trabalhada do {nome}: "))
sal = salario(horas,valorHora)
print(f"O salário do funcionário {nome} é R${sal}")