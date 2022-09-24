''' 115. Faça um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

calcula salário

receber a quantidade de horas trabalhadas
receber o valor da hora 
multiplicar o número de horas trabalhadas pelo valor da hora
mostrar o resultado da multiplicação'''

valor_por_hora = float(input('Qual valor você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou nesse mês? '))

salario = horas_trabalhadas * valor_por_hora

print('Neste mês você vai receber R$ {0:.2f}'.format(salario))
