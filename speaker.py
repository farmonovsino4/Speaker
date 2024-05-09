import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(word: str):
    engine.say(word)
    engine.runAndWait()

recognizer = speech_recognition.Recognizer()

speak("Hello ")
speak("what can i do for you")

def Alexa():
    global recognizer
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                print("Listening...")
                voice = recognizer.listen(mic)
                command = recognizer.recognize_google(voice)
                command = command.lower()
                if "hey alexa" in command:
                    command = command.replace('hey alexa', '')
                    print(command)
                else:
                    pass
        except speech_recognition.exceptions.UnknownValueError:
            pass
        return command
    
def RunAlexa():
    command = Alexa()
    if 'play' in command:
        song = command.replace('play', '')
        speak("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        speak("Current time is " + time)
    elif 'who is' in command:
        info = command.replace('who is', '')
        speak("searching " + info)
        try:
            wiki = wikipedia.summary(info, 1)
        except:
            speak("I could not find " + info)
            print("I could not find")
        else:
            print(wiki)
            speak(wiki)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    

while True:
    RunAlexa()