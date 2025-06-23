# entrada dos valores
eficiencia = int(input("Pontuação da eficiência: "))
colaboracao = int(input("Pontuação da colaboração: "))

# condicional
if eficiencia >= 80:
    if colaboracao >= 70:
        classificacao = "Excelente"
    else:
        classificacao = "Bom"

elif 50 <= eficiencia < 80:
    if colaboracao >= 70:
        classificacao = "Satisfatório"
    else:
        classificacao = "Regular"

else:
    classificacao = "Insuficiente"

# Imprimir classificacao do usuario
print(f"A classificação de desempenho do usuário é: {classificacao}")
