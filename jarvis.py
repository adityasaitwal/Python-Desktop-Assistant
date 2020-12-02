import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, How can I help you?")

def takeCommand(): 
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() #This class helps us to recognize the audio
    with sr.Microphone(device_index=1) as source: 
        #This is used as a source microphone
        print("Listening...")
        r.pause_threshold = 1 #some seconds of non-speaking audio before a phrase is considered as complete
        audio = r.listen(source)

    try: 
        print("Recognizing... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please... ")
        return "None"    
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\dell\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send your email to your destination")

        elif 'who are you' in query:
            speak("I am your personal desktop assistant jarvis") 

        elif 'close jarvis' in query:
            speak("OK Sir,Have a good day and See you soon")
            exit()



      
