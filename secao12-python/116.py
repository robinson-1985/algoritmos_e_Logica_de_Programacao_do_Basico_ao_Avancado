'''116. Faça um algoritmo tendo como dados de entrada a altura de uma pessoa, calcule o seu peso ideal,
usando a seguinte fórmula: (72.7 * altura) - 58

calcula peso ideal

receber a altura da pessoa
multiplicar a altura por 72.7
diminuir 58 do resultado da multiplicação
mostrar o valor da subtração.'''

altura = float(input('Qual a sua altura? '))

peso_ideal = (72.7 * altura) - 58

print('Seu peso ideal seria {0:.2f}'.format(peso_ideal))
