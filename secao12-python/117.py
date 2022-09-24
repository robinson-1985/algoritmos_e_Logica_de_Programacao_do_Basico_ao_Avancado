''' 117. Ler uma variável numérica n e imprimi-lá somente se for maior que 100, caso contrário imprima
com o valor zero.

receber valor
se valor > 100 então
    escrever valor
senão
    valor = 0
    escrever valor'''

n = int(input('Informe um número: '))

if n > 100:
    print(n)
else:
    n = 0
    print(n)
