'''5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
1,68 e pese 75kg'''


peso = 75
altura = 1.68
def IMC(peso,altura):
    imc = peso /(altura**2)
    return imc


result = IMC(peso, altura) 
print(f'O calculo IMC de uma pessoa com peso {peso} e altura {altura} é igual a { result:.2f}')

 
