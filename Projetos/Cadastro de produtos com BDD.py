from banco import conectar
def adicionar_produto():
    print("\n--- ADICIONAR PRODUTO ---")

    descricao = input("Descrição do produto: ")

    try:
        preco = float(input("Preço do produto: "))
        if preco < 0:
            print("O preço não pode ser negativo!")
            return
    except ValueError:
        print("Digite um preço válido!")
        return

    conexao = conectar()

    conexao.execute(
        "INSERT INTO produtos (descricao, preco) VALUES (?, ?)",
        (descricao, preco)
    )

    conexao.commit()
    conexao.close()

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")

    conexao = conectar()

    cursor = conexao.execute(
        "SELECT id, descricao, preco FROM produtos ORDER BY id"
    )

    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
    else:
        for produto in produtos:
            print(
                f"ID: {produto[0]} | "
                f"Produto: {produto[1]} | "
                f"Preço: R$ {produto[2]:.2f}"
            )

    conexao.close()


def editar_produto():
    print("\n--- EDITAR PRODUTO ---")

    conexao = conectar()

    produtos = conexao.execute(
        "SELECT id, descricao, preco FROM produtos ORDER BY id"
    ).fetchall()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        conexao.close()
        return

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Produto: {produto[1]} | "
            f"Preço: R$ {produto[2]:.2f}"
        )

    try:
        codigo = int(input("Digite o ID do produto que deseja editar: "))
    except ValueError:
        print("Digite um ID válido!")
        conexao.close()
        return

    produto = conexao.execute(
        "SELECT id FROM produtos WHERE id = ?",
        (codigo,)
    ).fetchone()

    if produto is None:
        print("ID não encontrado!")
        conexao.close()
        return

    nova_descricao = input("Digite a nova descrição: ")

    try:
        novo_preco = float(input("Digite o novo preço: "))
        if novo_preco < 0:
            print("O preço não pode ser negativo!")
            conexao.close()
            return
    except ValueError:
        print("Digite um preço válido!")
        conexao.close()
        return

    conexao.execute(
        "UPDATE produtos SET descricao = ?, preco = ? WHERE id = ?",
        (nova_descricao, novo_preco, codigo)
    )

    conexao.commit()
    conexao.close()

    print("Produto editado com sucesso!")


def deletar_produto():
    print("\n--- EXCLUIR PRODUTO ---")

    conexao = conectar()

    produtos = conexao.execute(
        "SELECT id, descricao, preco FROM produtos ORDER BY id"
    ).fetchall()

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        conexao.close()
        return

    for produto in produtos:
        print(
            f"ID: {produto[0]} | "
            f"Produto: {produto[1]} | "
            f"Preço: R$ {produto[2]:.2f}"
        )

    try:
        codigo = int(input("Digite o ID do produto que deseja excluir: "))
    except ValueError:
        print("Digite um ID válido!")
        conexao.close()
        return

    produto = conexao.execute(
        "SELECT descricao FROM produtos WHERE id = ?",
        (codigo,)
    ).fetchone()

    if produto is None:
        print("ID não encontrado!")
        conexao.close()
        return

    conexao.execute(
        "DELETE FROM produtos WHERE id = ?",
        (codigo,)
    )

    conexao.commit()
    conexao.close()

    print(f"Produto '{produto[0]}' excluído com sucesso!")


opcao = -1

while opcao != 0:
    print("\n================================")
    print("      CADASTRO DE PRODUTOS")
    print("================================")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Editar produto")
    print("4 - Excluir produto")
    print("0 - Sair")
    print("================================")

    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite uma opção válida!")
        continue

    if opcao == 1:
        adicionar_produto()

    elif opcao == 2:
        listar_produtos()

    elif opcao == 3:
        editar_produto()

    elif opcao == 4:
        deletar_produto()

    elif opcao == 0:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")
