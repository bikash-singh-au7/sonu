import pyttsx3 # It is text to speech module (pip install pyttsx3)
import speech_recognition as sr # This is speech recognition module (pip install speechRecognition)
import datetime
import time
# import wikipedia # This is wekipedia python module (pip install wikipedia)
# import webbrowser
# import os
# import smtplib # This module helps to send the emails

# Create a engine
engine = pyttsx3.init()

# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
# Girl voice
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('voice', en_voice_id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour > 5 and hour <= 12:
        speak("Hi Good Morning Akash, I am Sonu. How may i help you sir")
    elif hour > 12 and hour < 18:
        speak("Hi Good Afternoon Akash, I am Sonu. How may i help you sir")
    else:
        speak("Hi Good Evening Akash, I am Sonu. How may i help you sir")
def takeCommand():
    query = "Try Again"
    # Crete a object
    r = sr.Recognizer()
    
    # Create Microphone
    m = sr.Microphone()

    # Open microphone as audio source 
    with m as source:
        print("Listining...")
        # Store audio in audio variable
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        # convert audio into text
        query = r.recognize_google(audio)
    except:
        pass

    if query == "hey what is my name":
        speak("Your name is Akash")
    elif query == "what is time":
        pass
    elif query == "what is my age":
        speak("your are 21 year old")
    elif query == "what is my village":
        speak("your village is pipra")
    elif query == "who is my friend":
        speak("Your friend is Ashutosh")
    elif query == "exit":
        speak("Good bye")
        exit()

    else:
        speak("I dont recognize your voice speak again")
    
    takeCommand()
if __name__ == "__main__":
    wishMe()
    takeCommand()
# ==================Refrences=========================
# Change the language 
# 1) https://www.devdungeon.com/content/text-speech-python-pyttsx3#install_package