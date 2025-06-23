# coletando dados do usuário
nome = str(input("Informe seu nome: "))
altura = float(input("Insira sua altura em metros: "))
peso = float(input("Insira seu peso em kg: "))

imc = peso / altura ** 2

# Exibindo o resultado
print(f"{nome} tem IMC igual a {imc:.2f}")
