#importing required packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()       #creating a listener by calling the speech recognition package
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[1].id)
def talk(text):                  #creating a function to talk back
    engine.say(text)
    engine.runAndWait()
def accept_command():            #creating a function to get input from the microphone
   try:
       with sr.Microphone() as source:
           print("listening..")
           voice = listener.listen(source)
           command = listener.recognize_google(voice)
           command = command.lower()
           if "blackie " in command:
               command = command.replace("blackie","")
               print(command)
   except:
        pass
   return command
def run_asst():
    command = accept_command()
    print(command)
    if "who are you" in command:
        talk("i am a simple voice assistant to make your task easy")
    elif "play "  in command:
        song = command.replace("play" , '')
        talk("playing.." + song  )
        pywhatkit.playonyt(song)
    elif "time " in command:
        time = datetime.datetime.now().strftime("%H:  %M")
        talk("current time is " + time)
        print(time)
    elif "who" or "what" in command:
        person = command.replace("who" , "")
        info = wikipedia.summary(person,3)
        print(info)
        talk (info)
    else:
        talk("Sorry,can you say it again")

run_asst()
