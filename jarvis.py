import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0 ].id)


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
    with sr.Microphone() as source: 
        #This is used as a source microphone
        print("Listening...")
        r.pause_threshold = 1 #some seconds of non-speaking audio before a phrase is considered as complete
        audio = r.listen(source)

    try: 
        print("Recognizing... ")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please... ")
        return "None"    
    return query    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
      
    