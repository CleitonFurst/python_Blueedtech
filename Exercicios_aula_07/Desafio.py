'''DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no
formato DD/MM/AAAA e devolva uma string no formato DD de mes Por Extenso de AAAA.
Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que
Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro
terá 29 dias.'''




def data_escrita(data):
    mes = data[3:5]
    ano = data[6:]
    dia = data[:2]
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
           return True
    # Meses com 30 dias
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            return True    
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29:
                return True
        elif dia <= 28:
                return True
        else:
            return 'Mês invalido'
    else:
         return 'Mês invalido'





