# Tabuada

# repetição
while True:
    numero = int(input("Digite o número: "))
    if numero < 0:
        print("Programa encerrado")
        break
    if numero == 0:
        print("Numero zero ignorado.")
        continue
    print(f"Tabuada do número {numero}: ")

    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")
