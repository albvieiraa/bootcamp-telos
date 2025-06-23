'''
# Objetivo: Criar um programa que permite:
1. Cadastrar usuários com nome, idade, cidade e id
2. Listar todos os usários cadastrados
3. Filtar usuários por idade mínima
4. Exibir estatísticas básicas sobre os usuários

'''

# Passo 1: Criando a Estrutura de Dados
usuarios = {}
proximo_id = 1

# Passo 2: Criar funções para o cadastro
def cadastrar_usuario(nome, idade, cidade):
    global proximo_id
    usuarios[proximo_id] = {"nome": nome, "idade": idade, "cidade": cidade}
    print(f"Usuário {nome} cadastrado com suceddo! ID: {proximo_id}")
    proximo_id += 1 # incremento

# Passo 3: Funções para analise dos usuários

    # Listar usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    print("\nLista de usuários: ")
    for id, dados in usuarios.items():
        print(f"ID:{id} | Nome: {dados["nome"]} | Idade: {dados["idade"]} | Cidade: {dados["cidade"]}")

    # Filtrar usuários por idade mínima
              
def filtrar_por_idade(idade_minima):
    filtrados = {id: dados for id, dados in usuarios.items() if int(dados["idade"]) >= idade_minima}
    if not filtrados:
        print(f"Nenhum usuário encontrado com idade maior ou igual a {idade_minima}.\n")
        return
    print(f"\nUsuários com idade maior ou igual a {idade_minima}:")
    for id, dados in filtrados.items():
        print(f"ID:{id} | Nome: {dados["nome"]} | Idade: {dados["idade"]} | Cidade: {dados["cidade"]}")
    
    
    # Exibir estatísticas gerais
def estatisticas_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return

    total = len(usuarios)
    idades = [int(dados["idade"]) for dados in usuarios.values()]
    idade_media = round((sum(idades) / total),2)
    idade_max = max(idades)
    idade_min = min(idades)

    print("\n Estatísticas dos Usuários:")
    print(f"Total de usuários: {total}")
    print(f"Idade média: {idade_media}")
    print(f"Idade máxima: {idade_max}")
    print(f"Idade mínima: {idade_min}")
        

# Passo 4: Criar Menu Interativo

def menu():
    while True:
        print("\n MENU DO SISTEMA DE USUÁRIOS")
        print("1. Cadastrar um novo usuário.")
        print("2. Listar todos os usuários.")
        print("3. Filtrar usuários por idade mínima.")
        print("4. Exibir estatísticas básicas.")
        print("5. Sair.")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            cidade = input("Cidade: ")
            cadastrar_usuario(nome, idade, cidade)
            
        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            idade_minima = int(input("Digite a idade mínima: "))
            filtrar_por_idade(idade_minima)

        elif opcao == "4":
            estatisticas_usuarios()

        elif opcao == "5":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

menu()
