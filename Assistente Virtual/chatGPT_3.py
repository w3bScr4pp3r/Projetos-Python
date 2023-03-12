import speech_recognition as sr
import openai
import pyttsx3

engine = pyttsx3.init()

# Configurar a chave de API do OpenAI
openai.api_key = "KEY_API_OPENAI"

def chat():
    # Inicia a captura de áudio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)

    try:
        # Reconhece o áudio
        print("Processando...")
        query = r.recognize_google(audio, language="pt-BR")
        print(f"Você: {query}")

        # Envia a consulta para o modelo de linguagem do OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=query,
            temperature=0.5,
            max_tokens=1500,
            n=1,
            stop=None,
            timeout=15,
        )

        # Obtém a resposta do modelo
        answer = response.choices[0].text.strip()
        print(f"ChatGPT: {answer}")

        # Converte a resposta em fala
        engine.say(answer)
        engine.runAndWait()

    except Exception as e:
        print(f"Erro: {str(e)}")

while True:
    chat()
