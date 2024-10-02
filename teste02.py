option = 0
produtos = {
    "Camiseta": {"Nome": "Camiseta", "Quantidade": 20, "Preço": 35.5},
    "Calça": {"Nome": "Calça", "Quantidade": 15, "Preço": 79.9}
}

def actions():
    print("1. Adicionar novo produto \n2. Visualizar estoque \n3. Atualizar quantidade de produto \n4. Mostrar valor total do estoque \n5. Sair")
    global option
    option = int(input("Escolha uma opção: "))
    return option

def adicionarProduto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    produtos[nome] = {"Nome": nome, "Quantidade": quantidade, "Preço": preco}  # Corrigido para usar colchetes []
    print(f"Produto '{nome}' adicionado com sucesso!")

def visualizarProduto():
    if produtos:
        print("Estoque atual:")
        for nome, info in produtos.items():
            print(f"- Produto: {info['Nome']}, Quantidade: {info['Quantidade']}, Preço: R${info['Preço']:.2f}")  # Formatação do preço
    else:
        print("Sem produtos no estoque")

def atualizarProduto():
    nome = input("Qual o nome do produto? ")
    if nome in produtos:
        quantidade = int(input("Qual a nova quantia? "))
        produtos[nome]["Quantidade"] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
    else:
        print("Produto não encontrado")

def valorTotal():
    valor = 0

    for produto in produtos:
        quantidade = produtos[produto]["Quantidade"]
        preco = produtos[produto]["Preço"]
        valor += quantidade * preco  

    print(f"Valor total do estoque: R${valor:.2f}") 

def action():
    if option == 1:
        adicionarProduto()
    elif option == 2:
        visualizarProduto()
    elif option == 3:
        atualizarProduto()
    elif option == 4:
        valorTotal()
    elif option == 5:
        print("Saindo do programa...")
        return False
    else:
        print("Essa opção não existe.")
    return True


continuar = True
while continuar:
    actions()
    continuar = action()
