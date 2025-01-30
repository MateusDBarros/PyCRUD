class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


def entrada_int(mensagem):
    """Solicita um número inteiro do usuário, garantindo que a entrada seja válida."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")


def criar_pessoa():
    """Cria um novo objeto Pessoa com os dados inseridos pelo usuário."""
    nome = input("Digite o nome da pessoa: ")
    idade = entrada_int("Digite a idade: ")
    return Pessoa(nome, idade)


def atualizar_pessoa(pessoa):
    """Atualiza os dados de uma pessoa, mantendo os valores antigos caso o usuário não os modifique."""
    nome = input(f"Atualizar nome ({pessoa.nome}): ") or pessoa.nome
    idade = input(f"Atualizar idade ({pessoa.idade}): ").strip()

    if idade.isdigit():  # Garante que o usuário digitou um número válido
        pessoa.idade = int(idade)

    pessoa.nome = nome


def deletar_pessoa(lista, indice):
    """Remove uma pessoa da lista com base no índice fornecido, se for válido."""
    if 0 <= indice < len(lista):
        pessoa_removida = lista.pop(indice)  # `.pop()` retorna o elemento removido
        print(f"Pessoa '{pessoa_removida.nome}' removida com sucesso.")
    else:
        print("Erro: Índice inválido! Nenhuma pessoa foi removida.")


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
        if lista_de_pessoas:
            indice = entrada_int("Digite o índice da pessoa a ser atualizada: ")
            if 0 <= indice < len(lista_de_pessoas):
                atualizar_pessoa(lista_de_pessoas[indice])
            else:
                print("Erro: Índice inválido!")
        else:
            print("A lista está vazia. Nenhuma pessoa para atualizar.")
    elif escolha == '3':
        if lista_de_pessoas:
            indice = entrada_int("Digite o índice da pessoa a ser deletada: ")
            deletar_pessoa(lista_de_pessoas, indice)
        else:
            print("A lista está vazia. Nenhuma pessoa para deletar.")
    elif escolha == '4':
        if lista_de_pessoas:
            for i, pessoa in enumerate(lista_de_pessoas):
                print(f"{i}: {pessoa}")
        else:
            print("A lista está vazia.")
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
