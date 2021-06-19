from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import pyaudio


r = sr.Recognizer()


def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Malesef anlayamadım.")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")
        return voice

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


def response(voice):
    if "merhaba" in voice:
        speak("sanada merhaba")

    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")

    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")

    if "hangi gündeyiz" in voice or "bugün günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"
        speak("bugün günlerden " + today)

    if "saat kaç" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)

    if "görüşürüz" in voice:
        speak("görüşürüz canım")
        exit()

# playsound("DING.mp3")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)