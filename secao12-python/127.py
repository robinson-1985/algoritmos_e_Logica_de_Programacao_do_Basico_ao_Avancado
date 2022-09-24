''' 127. Faça um algoritmo que determine o maior entre N números. A condição de parada é a entrada de um 
valor 0, ou seja, o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0

maior = 0
receber valor
enquanto valor != 0 processar 
    se valor > maior então
        maior = valor
    receber valor
escrever "Maior valor" + maior '''

maior = 0

n = int(input('Informe um número: '))

while n != 0:
    if n > maior:
        maior = n
    n = int(input('Informe um número: '))
print('O maior número é {0}'.format(maior))
