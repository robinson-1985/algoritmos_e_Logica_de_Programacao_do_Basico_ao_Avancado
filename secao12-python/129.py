''' 129. Elabore um programa que gera e escreve os números ímpares dos números entre 100 e 200

para i = 100, enquanto i <= 200 processar
    se (i % 2 != 0) então
        escrever "Impar: " + i'''

for i in range(100, 201):
    if i % 2 != 0:
        print(i)
