"""                                  ГЛАВНЫЙ КОД ГОЛОСОВОГО ПОМОЩНИКА ТОБИ!                                          """
"""            ЭТО - МОЗГ ТОБИ, 'ДОБРО ПОЖАЛОВАТЬ' - СКАЗАЛ ОН! УСЛОВНО ЗДЕСЬ ВСЯ ЕГО МЕХАНИКА И МОДУЛИ:)            """

# Библиотеки
import speech_recognition
from toby_cfg import *
import pyttsx3
import datetime
import os
import webbrowser


sr = speech_recognition.Recognizer()

sr.pause_threshold = 0.5

toby_name = "доби"



#  Захват Входящего Сообщения:
def voice_handler():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return "Я тебя не понял!"

def general():
    global engine
    while True:
        query = voice_handler() # Текст, который берется с микрофона
# Музыка
        if "включи музыку" in query:
            play_music()
        elif "останови музыку" in query:
            stop_music()

# Остановка программы
        elif "стоп" in query:
            break

# Стандартные Вопросы
        elif "привет" in query or "здарова" in query:
            greeting()
        elif "как дела" in query:
            speak(random.choice(answers_HowAreYou))
        elif "что делаешь" in query or "что делаешь" in query:
            speak(random.choice(answers_WhatYouDo))
        elif "время" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Сейчас {strTime}")

# Открытие YouTube
        elif 'открой хостинг' in query or "хостинг" in query:
            webbrowser.open("https://www.youtube.com/")

# Открытие Гугл:
        elif 'открой браузер' in query or "браузер" in query:
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")

# Открытие Дискорда
        elif "открой дискорд" in query or "голос" in query:
            os.startfile(r"C:\Users\kleno\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")


# Открытие IDE
        elif 'открой вс' in query:
            codePath = r"C:\Users\kleno\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code" #путь к приложению
            os.startfile(codePath)
        elif 'открой пайчарм' in query or "открой пичарм" in query:
            codePath2 = r"C:\Users\kleno\OneDrive\Рабочий стол\PyCharm Community Edition 2021.2.2.lnk" #путь к приложению
            os.startfile(codePath2)

if __name__ == "__main__":
    general()
