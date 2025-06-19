#### Criando um Sistema de Perguntas e Respostas

<<<<<<< HEAD
# Passo 1: Importar biblioteca
import unicodedata

# Passo 2: Criar um dicionário com as perguntas e respostas
=======
# Passo 1: Importar bibliotecas
import unicodedata

# Passo 2: Criar um dicionário com as perguntas e respostas
>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1
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

<<<<<<< HEAD
# Passo 3: Criar função para limpeza do input
def limpar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto) # separar os caracteres especiais
    texto = texto.encode('ascii', 'ignore').decode('utf-8') # remover os caracteres especiais
    texto = texto.strip()
    return texto
=======
# Passo 3: Criar função para limpeza do input
def limpar_texto(texto):
    texto = texto.lower() # minúsculas
    texto = unicodedata.normalize('NFD', texto) # "separa" possíveis caracteres especiais
    texto = texto.encode('ascii', 'ignore').decode('utf-8') # remove os caracteres especiais
    texto = texto.strip() # remove espaços em branco
    return texto
>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1

<<<<<<< HEAD
# Passo 4: Criar a lógica do quiz
=======
# Passo 4: Criar a lógica do quiz

>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1
acertos = 0
<<<<<<< HEAD

print("🧠 Bem-vindo(a) ao Quiz de Conhecimentos Gerais!\n")

=======
print("🧠 Bem-vindo(a) ao Quiz de Conhecimentos Gerais!\n")
>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1
for pergunta, resposta in quiz.items():
    resposta_usuario = input(pergunta + " ")

<<<<<<< HEAD
    # Limpar os textos para comparar corretamente
    if limpar_texto(resposta_usuario) == limpar_texto(resposta):
        print("✅ Resposta correta!\n")
=======
    # limpeza
    if limpar_texto(resposta_usuario) == limpar_texto(resposta):
        print("✅ Resposta correta!\n")
>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1
        acertos += 1
    else:
<<<<<<< HEAD
        print(f"❌ Resposta errada! A resposta correta é: {resposta}\n")
=======
        print(f"❌ Resposta errada! A resposta correta é: {resposta}\n")
        
print(f"🏁 Você acertou {acertos} de {len(quiz)}")
>>>>>>> 3df867fd802aa02ec7bba5ed4a377b061e0b30d1

print(f"🏁 Você acertou {acertos} de {len(quiz)} perguntas.")