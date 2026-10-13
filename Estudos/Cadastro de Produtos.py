produtos = []

def adicionar_produto(produtos):
    print("\n\nADICIONAR PRODUTO")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço do produto: "))
    produto = {f"descricao": descricao, "preco": preco}
    produtos.append(produto)
    print("Cadastro realizado com sucesso!")
    print("-------------------------------------------------------------------------------")

def listar_produtos(produtos):
    print('\n\nLISTA DE PRODUTO')
    for indice, produto in enumerate(produtos):
        print(f'{[indice]} ${produto["descricao"]} ... ${produto["preco"]}')
    print('\n\n')

def editar_produto(produtos):
    print("\n\nEDITAR PRODUTO")

    if len(produtos) == 0:
        print("-------------------------------------------------------------------------------")
        print("Nenhum produto cadastrado!")
        print("-------------------------------------------------------------------------------")
        return

    listar_produtos(produtos)

    codigo_do_produto = int(input("Digite o índice do produto que deseja editar: "))

    if codigo_do_produto >= 0 and codigo_do_produto < len(produtos):
        edit_desc = input("Digite a nova descrição do produto: ")
        edit_preco = float(input("Digite o novo preço do produto: "))

        produtos[codigo_do_produto]["descricao"] = edit_desc
        produtos[codigo_do_produto]["preco"] = edit_preco

        print("Produto editado com sucesso!")
    else:
        print("Índice inválido!")

    print("-------------------------------------------------------------------------------")
            

def deletar_produto(produtos):
    print("\n\nDELETAR PRODUTO")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado!")
        return

    listar_produtos(produtos)

    codigo_do_produto = int(input("Digite o índice do produto que deseja deletar: "))

    if codigo_do_produto >= 0 and codigo_do_produto < len(produtos):
        produto_removido = produtos.pop(codigo_do_produto)

        print(f"Produto '{produto_removido['descricao']}' deletado com sucesso!")
    else:
        print("Índice inválido!")

    print("-------------------------------------------------------------------------------")
  

opcao = -1
while(opcao != 0):
    print("CADASTRO DE PRODUTOS")
    print("-------------------------")
    print("1 - Adicionar produtos")
    print("2 - Listar produto")
    print("3 - Editar produto")
    print("4 - Deletar produto")
    print("-------------------------")
    print("0 - Sair")
    print("-------------------------")

    opcao = int(input("Digite a opcao desejada: "))

    if opcao == 0:
        break
    if opcao == 1:
        adicionar_produto(produtos)
    if opcao == 2:
        listar_produtos(produtos)
    if opcao == 3:
        editar_produto(produtos)
    if opcao == 4:
        deletar_produto(produtos)