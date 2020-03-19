import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS  

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            tobi_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            tobi_speak('Sorry i did not get that!')
        except sr.RequestError:
            tobi_speak('Sorry, my speech service is down!')
        return voice_data

def tobi_speak(audio_string):
    tts = gTTS(text=audio_string ,lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        tobi_speak('My name is tobi')
    if 'time ' in voice_data:
        tobi_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        tobi_speak('Here is what i found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.lk/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        tobi_speak('Here is the location for' + location)
    if 'exit' in voice_data:
        tobi_speak('Bye!')
        exit()
    

time.sleep(1)
tobi_speak('Hi im tobi,How can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)