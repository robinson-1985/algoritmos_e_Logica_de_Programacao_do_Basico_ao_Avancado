''' 131. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

escrever "Informe o nome"
receber nome
escrever "Informe a senha"
receber senha
enquanto senha == nome processar
    escrever "Senha não pode ser igual ao nome"
    escrever "Informe o nome"
    receber nome 
    escrever "Informe a senha"
    receber senha'''

nome = input("Informe o nome: ")
senha = input("Informe a senha: ")

while nome == senha:
    print("Nome de usuário e senha devem ser diferentes!\n")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")
