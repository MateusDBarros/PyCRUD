class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

def criar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade: "))
    return Pessoa(nome, idade)

def atualizar_pessoa(pessoa):
    nome = input(f"Atualizar nome ({pessoa.nome}): ") or pessoa.nome
    idade = input(f"Atualizar idade ({pessoa.idade}): ")
    if idade:
        pessoa.idade = int(idade)
    pessoa.nome = nome

def deletar_pessoa(lista, indice):
    if 0 <= indice < len(lista):
        del lista[indice]
    else:
        print("Índice inválido!")

lista_de_pessoas = []

while True:
    print("\n1. Adicionar pessoa")
    print("2. Atualizar pessoa")
    print("3. Deletar pessoa")
    print("4. Mostrar lista")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        pessoa = criar_pessoa()
        lista_de_pessoas.append(pessoa)
    elif escolha == '2':
        indice = int(input("Digite o índice da pessoa a ser atualizada: "))
        if 0 <= indice < len(lista_de_pessoas):
            atualizar_pessoa(lista_de_pessoas[indice])
        else:
            print("Índice inválido!")
    elif escolha == '3':
        indice = int(input("Digite o índice da pessoa a ser deletada: "))
        deletar_pessoa(lista_de_pessoas, indice)
    elif escolha == '4':
        for i, pessoa in enumerate(lista_de_pessoas):
            print(f"{i}: {pessoa}")
    elif escolha == '5':
        break
    else:
        print("Opção inválida! Tente novamente.")
