"""                                      КОНФИГ ГОЛОСОВОГО ПОМОЩНИКА ТОБИ!                                           """
""" В КОНФИГ ВХОДЯТ ОТВЕТЫ НА ВОПРОСЫ, А ТАКЖЕ СКРИПТЫ И ПАРСЕРЫ ДЛЯ ЕГО АДЕКВАТНОЙ РАБОТЫ! ВСЕ ОСТАЛЬНОЕ В ГЕНЕРАЛ  """

# Библиотеки
import os
import random
from pygame import mixer
import pyttsx3
import datetime

# Списки с ответами:
answers_HowAreYou = ["Норм", "Круто", "Лучше Чем у всех хуже чем у вас", "Пойдет", "Хорошо", "Нормально", "Отлично"]
answers_WhatYouDo = ["Занимаюсь Физикой", "Работаю", "Нажимаю Красную Кнопку", "Улучшаю ИИ"]

# Музыка(Флаг + Миксер)
mixer.init()
music = None

# Настройки Голоса
engine = pyttsx3.init()
voices = engine.getProperty('voices') #даёт подробности о текущем установленном голосе
engine.setProperty('voice', voices[0].id)  # 0-мужской , 1-женский

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Доброе Утро")       
    elif hour >= 12 and hour < 18:
        speak("Добрый День")           
    else:
        speak("Добрый Вечер") 
# Произношение Фразы
def speak(audio):   
    engine.say(audio)    
    engine.runAndWait()

# Включение Музыки
def play_music():
    global music
    music = mixer.Sound("Musicc\\" + random.choice(os.listdir("Musicc")))
    music.play()

# Выключение Музыки
def stop_music():
    if music:
        music.stop()
