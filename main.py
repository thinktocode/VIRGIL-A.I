import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from googlesearch import search 
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("My Name Is VIRGIL Sir. I am an Artificial Intelligence. I can do your daily tasks for you. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('EMAIL', 'PASSWORD')
    server.sendmail('singhnamanbir29@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'show me the video of my cars' in query:
            codepath = "E:\\Think Arduino\\Cars"
            os.startfile(codepath) 

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'i am feeling lonely' in query:
            speak("dont feel like that. i am here to talk to you")

        elif 'how are you' in query:
            speak("I am good. just give milk to the cat for me")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif"open arduino ide" in query:
            codepath = ('C:\\Program Files (x86)\\Arduino\\arduino')
            os.startfile(codePath) 



        elif 'open lcsc' in query:
            webbrowser.open("lcsc.com")


        elif "open flappy bird" in query:
            codePath = "C:\\Users\\Lenovo\\Desktop\\flappy_bird\\main"
            os.startfile(codePath)


        elif "open arduino site" in query:
            webbrowser.open("arduino.cc")


        elif"isro" in query:
            webbrowser.open("isro.gov.in")

        elif"worst hospital in the world" in query:
            webbrowser.open("sghshospitals.com")

        elif"open my certificates" in query:
            codepath = "C:\\Users\\Lenovo\\Desktop\\YOUTUBE"
            os.startfile(codepath)

        elif"open manav mangal smart school" in query:
            webbrowser.open("edusecure.in/ManavMangalMohali")
        


        elif 'email to Naman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "singhnamanbir29@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir Naman . I am not able to send this email")   