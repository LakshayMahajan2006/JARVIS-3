import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
from covid import Covid

covid=Covid()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome back sir")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!!!")

    else:
        speak("Good Evening!!")

   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en.in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again......")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif 'open steam' in query:
            codePath = "D:\\steam setup\\Steam.exe"
            os.startfile(codePath)    

        elif 'open cs' in query:
            codePath = "C:\\Users\\shash\\Desktop.exe"
            os.startfile(codePath)

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'bye' in query:
            speak("Bye sir")
            exit() 
        
        elif 'poweroff' in query:
            os.system("shutdown /s /t 1")

        elif 'youtube' in query:
            speak("Go check out new video of Sahil Gupta")  
        
        elif 'Jarvis you there' in query:
            speak("at you service sir")
        
        elif 'connection' in query:
            speak("check")
        
        elif 'say' in query:
            speak("I have been indeed uploaded sir, we are online and ready")
        
        elif 'who are you' in query:
            speak("I'm Just A Rather Very Intelligent System aka Jarvis sir ")

        
