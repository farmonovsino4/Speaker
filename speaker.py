import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import os

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
    elif "set the volume to " in command:
        volume = command.replace("set the volume to ", "")
        if int(volume) >= 0 and int(volume) <= 100:
            pyautogui.press("volumeup" if volume > 50 else "volumedown")
            speak("volume set to " + volume)
    elif "set the brightness to " in command:
        brightness = command.replace("set the brightness to ", "")
        if int(brightness) >= 0 and int(brightness) <= 100:
            pyautogui.press("volumeup" if brightness > 50 else "volumedown")
            speak("brightness set to " + brightness)
    elif 'open projects folder' in command:
        speak("opening projects folder")
        os.startfile("C:\\Users\\User\\Documents\\projects")
    elif 'open downloads folder' in command:
        speak("opening downloads folder")
        os.startfile("C:\\Users\\User\\Downloads")
    elif 'open documents folder' in command:
        speak("opening documents folder")
        os.startfile("C:\\Users\\User\\Documents")

    

while True:
    RunAlexa()