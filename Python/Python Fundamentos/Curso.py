from usuario import Usuario
lista = []
continuar = " "
while continuar != "N":
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    sobrenome = input("Digite o seu sobrenome: ")
    user = Usuario(nome, idade, sobrenome)
    lista.append(user)
    continuar = input("Deseja continuar? (S/N) ")
else:
    for i in lista:
        print(f"Nome completo: {i.nome} {i.sobrenome} - Idade: {i.idade}")
    print("O cadastro finalizou")
