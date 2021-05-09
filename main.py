import speech_recognition as sr
import time 
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio =r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio, language="en-US")

        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendi')
        except sr.RequestError:
            alexa_speak('Lo siento, error de conexion')
        return voice_data


def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'Hola' in voice_data:
        alexa_speak('Hola, mi nombre es alexis')
    
    if 'search' in voice_data:
        buscar = record_audio('¿Que necesitas hacer?')
        url = 'https://www.youtube.com/results?search_query=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para:' + buscar)

    

    if 'good bye' in voice_data:
        exit()

time.sleep(1)
alexa_speak ('¿Como te puedo ayudar?')

while 1:
    voice_data = record_audio()
    respond(voice_data)

