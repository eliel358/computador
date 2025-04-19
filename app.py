import os
from langchain_ollama import OllamaLLM
# model = OllamaLLM(model="gemma3:1b")
# result = model.invoke(input='bom dia pode me falar hello word?')
# print(result)
def app():
    def listen():
        # os.system('cls')
        with sr.Microphone(device_index=1) as mic:
            # recognizer.adjust_for_ambient_noise(mic)
            print("Pode falar")
            audio = recognizer.listen(mic)
            try:
                audio = recognizer.recognize_google(audio,language='pt-br')
                print(audio)
                model = OllamaLLM(model="gemma3:1b")
                msg = ''
                
                if 'computador' in audio:
                    caracteres = [
                        '*','cmd', '#', '@', '&', '%', '$', '!', '+', '-', '=',
                        '~', '^', '`', ',',  ';', '"', "'", '<', '>', '(', ')',
                        '[', ']', '{', '}',
                        '😀', '😂', '🤣', '😊','😊', '😍', '😎', '😢', '😭', '😡', '🤔',
                        '👍', '👎', '🙏', '👏', '💪', '🔥', '💯', '❤️', '✨', '🎉',
                        '🎶', '🚀', '🐱', '🐶', '🌟', '🌈', '⚡', '☀️', '🌙', '🍀'
                    ]
                    result = model.invoke(input="escreva exatamente apenas o comando que devo escrever no prompt de comando do windows para fazer a seguinte ação   : "+audio+". caso queira use o site do google para abrir uma pesquisa no cmd")
                    for chunk in result:
                        if chunk not in caracteres:
                            msg= msg+(chunk)
                    print(msg)
                    os.system(msg)
                    listen()
                else:
                    caracteres = [
                    '*', '#', '@', '&', '%', '$', '!', '+', '-', '=', '/', '\\', '|',
                    '~', '^', '`',':', ';', '"', "'", '<', '>', '(', ')',
                    '[', ']', '{', '}',
                    '😀', '😂', '🤣', '😊','😊', '😍', '😎', '😢', '😭', '😡', '🤔',
                    '👍', '👎', '🙏', '👏', '💪', '🔥', '💯', '❤️', '✨', '🎉',
                    '🎶', '🚀', '🐱', '🐶', '🌟', '🌈', '⚡', '☀️', '🌙', '🍀'
                ]
                    result = model.invoke(input="responda resumidamente: "+audio)
                    for chunk in result:
                        if chunk not in caracteres:
                            msg= msg+(chunk)
                    print(msg)
                    talk(msg)
                    listen()
            except sr.UnknownValueError:
                print("não consegui entender")
                listen()
                

    def change_voice(words):
            os.system('cls')
            global voice_index
            change_voice_options = int(input("1-Escutar voz selecionada\n2-Trocar voz\n3-voltar\n(As vozes disponiveis dependem das que você tem instaladas no seu computador)\n"))
            
            if change_voice_options == 1:
                engine.setProperty('voice', voices[voice_index].id)
                engine.say(words)
                engine.runAndWait()
                change_voice(words)
            elif change_voice_options == 2:
                if voice_index == 0:
                    voice_index = 1
                elif voice_index == 1:
                    voice_index = 0
                change_voice(words)
            elif change_voice_options == 3:
                pass
            engine.setProperty('voice', voices[voice_index].id)
            engine.runAndWait()

    def talk(word):
            
        engine.setProperty('voice', voices[voice_index].id)
        engine.say(word)
        engine.runAndWait()



    print('1-Text to speech\n2-Speech to text')
    opcao = str(input('Escolha uma opção: '))
    if opcao == "1":
        word = input(str('Insira o texto: '))
        talk(word)

    if opcao == "2":
        listen()
try:
    import speech_recognition as sr
    import pyttsx3
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    voice_index = 0
    voices = engine.getProperty('voices')
    app()
except ModuleNotFoundError:
    install_library = str(input('Parece que você não tem as bibliotecas nescessarias para o app funcionar corretamente (SpeechRecognition e pyttsx3) \ndeseja instala-las? (S/N)\n'))
    if install_library == 's' or install_library == 'S':
        os.system('python -m pip install --upgrade pip')
        os.system('pip install SpeechRecognition')
        os.system('pip install pyttsx3')
        print('\nReinicie o app para funcionar\n')
    else:
        pass
