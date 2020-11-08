import os
from speak import takeCommand
from main import *
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
#to search, will ask search query at the time of execution




def music():
    print("Now Playing... Led Zeppelin X AC/DC Black in Black")
    led = "C:\\Users\\hp\\Desktop\\FRIDAY\\music\\acdc.mp3"
    os.startfile(led)
    return


def open_application(query):
    if "google" in query:
        speak("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in query or "mozilla" in query:
        speak("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    elif "word" in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
    elif "excel" in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    elif "code" in query:
        speak("Opening Visual Studio")
        os.startfile('C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
        return
    elif "spotify" in query:
        driver = webdriver.Chrome('E:\\FRIDAY\\chromedriver_win32\\chromedriver.exe')
        driver.get("https://open.spotify.com/")
        return


    else:
        speak("Application not available")
        return



def search_web(query):
    driver = webdriver.chrome('E:\\FRIDAY\\chromedriver_win32\\chromedriver.exe')
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in query.lower():
        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        query = query.split()[indx+1:]
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return
    else:
        if 'google' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(query.split()))
        return

