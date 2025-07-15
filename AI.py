import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import wolframalpha
import random

client = wolframalpha.Client('RKXJQE-UVJA44HREX')

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-10)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")    
    
    else:
        speak("Good Evening Sir!")

    speak("I am JARVIS, your Virtual Assistant. How can I help you?") 

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:    
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
       

        print("Sorry Sir! I didn't heard. Please Speak Again!") 
        return "None"  
    return query   

def sendEmail(to, content):   
    server = smtplib.SMTP('smtp.gmail.com', 587)    
    server.ehlo()
    server.starttls()
    server.login("shreyansh.coding@gmail.com", "rishu@testmail")
    server.sendmail("shreyansh.coding@gmail.com", to, content)
    server.close()

if __name__:"__main__"

wishme()

while True:
    query = takecommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("Wikipedia","")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open('youtube.com')  

    elif 'open chrome' in query:
        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome")      

    elif 'open google' in query:
        webbrowser.open('google.com')

    elif 'open google play store' in query:
        webbrowser.open('play.google.com')         

    elif 'play music' in query:
        music_dir = 'C:\\Users\\Shreyansh Kumar\\Songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir , songs[0]))

    elif 'thank you' in query:
        speak('Its my pleasure Sir!')
            
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"Sir, the current time according to IST is {strTime}")   

    elif 'send email' in query:
        try:
            speak("What will be the content?")
            content = takecommand()
            to = "gyanandasingh@gmail.com"
            sendEmail(to, content)
            speak('Sir, Email is sent')
        except Exception as e:
            print(e)
            speak('Sorry Sir, Email cant be sent to the recipient.') 

    elif 'play videos' in query:
        video_dir = "C:\\Users\\Shreyansh Kumar\\Videos" 
        videos = os.listdir(video_dir)
        print(videos)
        os.startfile(os.path.join(video_dir, videos[2]))    

    elif 'open command prompt' in query:

        cmd = "C:\\Windows\\system32\\cmd"
        os.startfile(cmd)    
                    
    elif 'shutdown' in query or 'quit' in query or 'exit' in query:
        speak('Good bye Sir! Have a Good Day')
        exit()      

    elif 'open control panel' in query:
        panel = "C:\\Users\\Shreyansh Kumar\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
        os.startfile(panel)

    elif 'what can you do' in query:
        speak("Sir! I am JARVIS the A.I. Sir I can open the apps you want, send emails to the person you want, play songs and videos, open games if you have any, i can also tell weather, meanings, or any other info you want to know, and if you dont want to make me do anything then just say shutdown or exit and I will leave. Thats all I can do!")       

    else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                    speak(results)
                        
                except:
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
            
            except:
                webbrowser.open('www.google.com')
