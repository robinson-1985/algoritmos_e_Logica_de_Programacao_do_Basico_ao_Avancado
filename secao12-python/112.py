''' 112. Faça um algoritmo para calcular o estoque médio de uma peça, sendo que:

estoque_medio = (quantidade_minima + quantidade_maxima) / 2

calcular o estoque médio
receber quantidade_minima
receber quantidade_maxima
somar quantidade_minima e quantidade_maxima
dividir o resultado da soma por 2
mostrar o resultado da divisão'''

quantidade_minima = int(input('Informe a quantidade minima: '))
quantidade_maxima = int(input('Informe a quantidade máxima: '))

estoque_medio = (quantidade_minima + quantidade_maxima) / 2

print('O estoque médio é {0}'.format(estoque_medio))
