import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        text = r.recognize_google(audio,language='en-US')
        print("You : ", text)
        return text 
    except:
        print("...")
        return "None"    
    return text


