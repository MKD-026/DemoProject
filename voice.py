import requests
from bs4 import BeautifulSoup
import speech_recognition as sr

listener = sr.Recognizer()
mic = sr.Microphone()
try:
    with mic as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(voice)
except:
    #print('Sorry I did not understand that. Can you tell it again?')
    pass