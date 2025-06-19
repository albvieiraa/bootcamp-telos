#### Criando um Sistema de Perguntas e Respostas

# Passo 1: Criar um dicionário com as perguntas e respostas
quiz = {
    "Qual é o maior planeta do sistema solar?": "Júpiter",
    "Em que continente fica o Brasil?": "América do Sul",
    "Quem pintou a Mona Lisa?": "Leonardo da Vinci",
    "Qual é o elemento químico representado pelo símbolo O?": "Oxigênio",
    "Qual é o animal terrestre mais rápido do mundo?": "Guepardo",
    "Qual é a capital da França?": "Paris",
    "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
    "Em que ano o homem pisou na Lua pela primeira vez?": "1969",
    "Qual é o rio mais longo do mundo?": "Rio Nilo",
    "Quem foi o primeiro presidente do Brasil?": "Deodoro da Fonseca"
}

# Passo 2: Criar a lógica do quiz

acertos = 0
for pergunta, resposta in quiz.items():
    resposta_usuario = input(pergunta + " ")

    if resposta_usuario.strip().lower() == resposta.lower():
        print("Resposta correta")
        acertos += 1
    else:
        print(f"Resposta errada! Resposta correta é: {resposta}")
print(f"Você acertou {acertos} de {len(quiz)}")
