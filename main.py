#import wikipedia
import subprocess
import os
import time
import datetime
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
from playsound import playsound
from speak import *
from libraries import *
from colors import *




def wish():
    os.system("cls")
    f  = open("text.txt","r")
    ascii = "".join(f.readlines())
    print(text(ascii)) 
    speak("Welcome,,Boss")

def note(text):
            speak("What should I name it")
            marknote = takeCommand()
            file_name = (f"{marknote}.txt")
            with open(file_name, "w") as f:
                f.write(text)
            subprocess.Popen(["notepad.exe", file_name])


if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or "tell me about" in query: #and now we know alan walker's faded won platinum records in 14 countries
            speak('Searching')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "beat drop" in query or "song" in query or "music" in query or "play" in query:
            music()
        
        elif "make a note" in query or "write this down" in query or "remember this" in query or "start" in query:
            speak("What would you like me to write down?")
            note_text = takeCommand()
            note(note_text)
            speak("I've made a note of that.")

        elif "show my private files" in query or "enter prior mode" in query or "private" in query:
            speak("voice activation required")
            e_passcode = takeCommand().lower()
            v_passcode = "cat"
            if e_passcode == v_passcode:
                speak("Welcome! Mr.Stark")
            else:
                speak("access denied")

        elif "blaze protocol" in query or "Blaze" in query:
            f  = open("blaze.txt","r")
            ascii = "".join(f.readlines())
            print(text(ascii)) 
            time.sleep(1.4)
            print("Iniating...")
            time.sleep(2.4)
            print("Conneted \ \ \ \n ")
            speak("what would you will like me to do")
            takeCommand()
            time.sleep(1.4)
            speak("completed")

        elif 'open' in query:
            open_application(query)
        

        elif "how are you" in query:
            speak("I am fine")

        elif "the time" in query or "time" in query or "clock" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir time is {strTime}")
            print(f"Sir, Time is {strTime}")

        elif "exit" in query or "deactivate" in query or "go " in query or "sleep" in query:
            speak("Deactivating Sir...")
            exit()
        
