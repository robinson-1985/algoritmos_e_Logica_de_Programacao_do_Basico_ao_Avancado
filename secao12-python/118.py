''' 118. Elabore um algoritmo que leia um número. Se positivo armazene-o em a, se for negativo, em b. No
final mostrar o resultado.

receber valor 
se valor > 0 então
    a = valor
    escrever "Valor positivo"
    escrever a 
senão
    b = valor
    escrever "Valor negativo"
    escrever b'''

numero = int(input('Informe um número: '))

if numero > 0:
    a = numero
    print('Valor positivo')
else:
    b = numero
    print('Valor negativo')
print(numero)
