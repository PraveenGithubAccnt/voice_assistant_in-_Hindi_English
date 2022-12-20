import pyttsx3
import speech_recognition as sr
from subprocess import call

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 160)
    engine.say(audio)
    engine.runAndWait()


def say(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		say("Listening your voice , chose your friendly language")
		print("Listening your voice...")
		r.pause_threshold = 1
		audio = r.listen(source)
        
	try:
		print("Recognizing...")
		lang = r.recognize_google(audio, language ='en-in')
		print(f"User said: {lang}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"	
	return lang  

def open_en():
    call(["python", "eng_va.py"])

def open_hi():
    call(["python", "hindi_va.py"])
   


print("\n")
print("chose your friendly language between English/Hindi \n")
print("अंग्रेजी/हिंदी में से अपनी भाषा का चुनाव करें")
speak("अंग्रेजी/हिंदी में से अपनी स्वतंत्र भाषा का चुनाव करें")
lng=takeCommand()
print(lng)

if lng=="Hindi":
    open_hi() 

else:
    open_en()
    
