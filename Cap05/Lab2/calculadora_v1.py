# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

import sys

def soma():
    x,y = recebe_dois_numeros(1)
    resultado = x + y
    imprime_operacao(x,y,resultado,1)

def subtracao():
    x,y = recebe_dois_numeros(2)
    resultado = x - y
    imprime_operacao(x,y,resultado,2)

def multiplicacao():
    x,y = recebe_dois_numeros(3)
    resultado = x * y
    imprime_operacao(x,y,resultado,3)

def divisao():
    x,y = recebe_dois_numeros(4)
    resultado = x / y
    imprime_operacao(x,y,resultado,4)

def imprime_operacao(x,y,resultado,numero_operacao):
    if numero_operacao == 1:
        sinal = " + "
    elif numero_operacao == 2:
        sinal = " - "
    elif numero_operacao == 2:
        sinal = " - "
    else:
        sinal = "/"

    print("\n " + str(x) + sinal + str(y) + " = " + str(resultado))

def encerra():
    print("\nObrigado por usar a calculadora.")
    sys.exit()

def recebe_dois_numeros(numero_operacao):
    x = int(input('Informe o primeiro número: '))
    segundo_numero_valido = False
    while segundo_numero_valido != True:
        y = int(input('Informe o segundo número: '))
        if numero_operacao == 4 and y == 0:
            print("\nNão existe divisão por zero. Informe outro valor")
        else:
            segundo_numero_valido = True
    return x,y

print("\n******************* Calculadora em Python *******************")

print("\nSelecione o número da opção desejada:")
print("\n1 - Soma")
print("\n2 - Subtração")
print("\n3 - Multiplicação")
print("\n4 - Divisão")
print("\n5 - Encerrar")

operacao_valida = False
while operacao_valida != True:
    operacao = int(input("\n\nDigite sua opção (1/2/3/4/5): "))
    if operacao < 1 or operacao > 5:
        print("\nA opção informada não existe.")
    else:
        operacao_valida = True

if operacao == 1:
   soma()
elif operacao == 2:
   subtracao()
elif operacao == 3:
   multiplicacao()
elif operacao == 4:
   divisao()
else:
   encerra()

