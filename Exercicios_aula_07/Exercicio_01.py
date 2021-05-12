'''1. Faça um programa, com uma função que necessita de três argumentos, e que forneça a
soma três três argumentos. '''


def  soma ( x , y , z ):
    soma  =  x  +  y  +  z
    print ( f'A soma dos valores é igual á { soma } ' )


valor1  =  float ( input ( 'Digite o primeiro valor:' ))
valor2  =  float ( input ( 'Digite o seundo valor:' ))
valor3  =  float ( input ( 'Digite o terceiro valor:' ))

soma ( valor1 , valor2 , valor3 )