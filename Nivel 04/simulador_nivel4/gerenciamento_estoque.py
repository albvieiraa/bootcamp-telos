'''Sistema de Gerenciamento de Estoque - RetailCo'''

# Dicionário para armazenar os produtos
estoque = {}


# Criar Menu
def mostrar_menu():
    print("\n***** Menu de Gerenciamento de Estoque *****")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade")
    print("3. Aplicar Desconto")
    print("4. Exibir Total do Estoque")
    print("5. Exibir Lista de Produtos")
    print("6. Sair")

#Função Adicionar produtos
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade inicial: "))
    preco = float(input("Digite o preço unitário: "))
    estoque[nome] = {'quantidade': quantidade, 'preco': preco}

# Atualizar produtos
def atualizar_quantidade():
    nome = input("Digite o nome do produto para atualizar a quantidade: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a quantidade a adicionar: "))
        estoque[nome]['quantidade'] += nova_quantidade
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado no estoque.")
        
# Aplicar desconto
def aplicar_desconto():
    nome = input("Digite o nome do produto para aplicar desconto: ").strip()
    if nome in estoque:
        desconto = float(input("Digite o valor do desconto (%): "))
        preco_atual = estoque[nome]['preco']
        novo_preco = preco_atual * (1 - desconto / 100)
        estoque[nome]['preco'] = round(novo_preco, 2)
        print(f"Desconto de {desconto}% aplicado ao produto '{nome}'. Novo preço: R${novo_preco:.2f}")
    else:
        print("Produto não encontrado.")

# Exibir preço total
def exibir_total():
    total = 0.0
    for produto, info in estoque.items():
        total += info['quantidade'] * info['preco']
    print(f"\n Valor total do estoque: R${total:.2f}")

# Exibir listagem de produtos
def exibir_produtos():
    if not estoque:
        print("\n Estoque vazio.")
    else:
        print("\n***** Lista de Produtos no Estoque *****")
        for produto, info in estoque.items():
            print(f"- Produto: {produto} | Quantidade: {info['quantidade']} | Preço: R${info['preco']:.2f}")

# Programa principal
while True:
    mostrar_menu()
    opcao = input("\nDigite o número da opção desejada: ").strip()

    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_quantidade()
    elif opcao == '3':
        aplicar_desconto()
    elif opcao == '4':
        exibir_total()
    elif opcao == '5':
        exibir_produtos()
    elif opcao == '6':
        print("\nEncerrando o sistema... Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1 a 6)")
