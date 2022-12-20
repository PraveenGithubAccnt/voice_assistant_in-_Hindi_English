import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import shutil
import pywhatkit as kit
import os

def say(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    engine.say(audio)
    engine.runAndWait()

def wishMe_en():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		say("Good Morning!")

	elif hour>= 12 and hour<18:
		say("Good Afternoon!")

	else:
		say("Good Evening!")
	
	say("I am your Assistant, saathee")

def username_en():
	say("What should i call you")
	uname = takeCommand_en()
	say("Welcome")
	say(uname)
	columns = shutil.get_terminal_size().columns
	
	print("##".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("##".center(columns))
	
	say("How can i Help you")

def takeCommand_en():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		say("Listening your voice")
		print("Listening your voice...")
		r.pause_threshold = 1
		audio = r.listen(source)
        
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"	
	return query  

if __name__ == '__main__':
        clear = lambda: os.system('cls')
        clear()
        wishMe_en()
        username_en()
        while True:
            query = takeCommand_en().lower()
            if 'how are you' in query:
                say("I am fine, Thank you")
                say("How are you, Sir")
            
            elif 'fine' in query or "good" in query:
                say("It's good to know that your fine")
            
            elif 'exit' in query or "stop" in query:
                say("Thanks for giving me your time")
                exit()
            
            elif 'time' in query :
                strtime = datetime.datetime.now().strftime('%H:%M:%S')
                say(f'the time is {strtime}')
            
            elif 'RGU website' in query or "rajiv gandhi" in query:
                say("Here you go to Rajiv Gandhi university website")
                webbrowser.open("https://rgu.ac.in/")

            elif 'Admission detail' in query or ' university admission' in query :
                say("Here you go to Rajiv Gandhi university admission portal")
                webbrowser.open("https://admissions.rgu.ac.in/") 

            elif 'wikipedia' in query or 'Search' in query:
                say('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                say("According to Wikipedia")
                print(results)
                say(results)
            
            elif 'youtube' in query:
                say('What do you want to play on Youtube, sir?')
                video = takeCommand_en().lower()
                say('Here you are going to youtube with your query')
                kit.playonyt(video)

            elif 'open google' in query:
                say('What do you want to search on Google')
                query = takeCommand_en().lower()
                say('Here you are going to google with your query')
                kit.search(query)	
            
            elif "who created you" in query or "made you" in query or "designed you" in query :
                say("i have been created by praveen , and the rest is a mystery")
			
            elif "hi" in query or "hello" in query:
                say("yes, how can i help you")
