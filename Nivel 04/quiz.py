#### Criando um Sistema de Perguntas e Respostas

# Passo 1: Importar biblioteca
import unicodedata

# Passo 2: Criar um dicionário com as perguntas e respostas
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

# Passo 3: Criar função para limpeza do input
def limpar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto) # separa os caracteres especiais
    texto = texto.encode('ascii', 'ignore').decode('utf-8') # ignora os caracteres especiais
    texto = texto.strip()
    return texto

# Passo 4: Criar a lógica do quiz
acertos = 0

print("🧠 Bem-vindo(a) ao Quiz de Conhecimentos Gerais!\n")

for pergunta, resposta in quiz.items():
    resposta_usuario = input(pergunta + " ")

    # Limpar os textos para comparar corretamente
    if limpar_texto(resposta_usuario) == limpar_texto(resposta):
        print("✅ Resposta correta!\n")
        acertos += 1
    else:
        print(f"❌ Resposta errada! A resposta correta é: {resposta}\n")

print(f"🏁 Você acertou {acertos} de {len(quiz)} perguntas.")
