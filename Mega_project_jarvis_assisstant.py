import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voice')
engine.setProperty('voice',voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("Hello i am AI Bot, How may i help you ")
    speak("Hello i am AI Bot, How may i help you ")
    speak("Please speak to enter your input")

def take():
    ''' This function will take the users microphonic input and print whatever user had said as a string '''

    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("\nListening....")
        r.pause_threshold=1
        audio =r.listen(Source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-id")
        print(f"user said : {query}")

    except Exception as e:
        print(e)
        print("Please say that again")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while 1:
        query=take().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia..")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="C:\\Users\\HP\\Desktop"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak("Sir the time is ")
            speak(strtime)

        elif 'date' in query:
            strdate=datetime.datetime.now().strftime("%Y-%m-%d")
            print(strdate)
            speak("Sir the Date is ")
            speak(strdate)





