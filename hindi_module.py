import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit as kit
import shutil
import os

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

def wishMe_hi():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("शुभ प्रभात!")

    elif hour>= 12 and hour<18:
        speak("नमस्कार!")

    else:
        speak("सुसंध्या!")
    
    speak("मैं आपका सहायक, साथी हूं")

def username_hi():
    speak("मैं आपको किस नाम से पुकारूं")
    uname = takeCommand_hi()
    speak("स्वागत है आपका")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("##".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("##".center(columns))
    speak("मैं आपकी क्या मदद कर सकता हूँ")

def takeCommand_hi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("आपकी आवाज सुनी जा रही है")  
        print('Listening your voice...')
        r.pause_threshold = 1
        audio = r.listen(source)
       
    try:
        print("Recognizing")
        Query = r.recognize_google(audio, language='hi-In')
        speak("आपने कहा: " + Query ) 
        print(f"User said: {Query}\n")
          
    except Exception as e:
        print(e)  			
        print("Say that again")
        return "None"
    return Query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    wishMe_hi()
    username_hi()
    while True:
        query=takeCommand_hi().lower()
        if 'यूट्यूब खोलो' in query or 'ओपन यूट्यूब' in query :
            speak("यूट्यूब खोला जा रहा है")
            webbrowser.open("youtube.com")
            
        elif 'गूगल खोलो' in query or 'ओपन खोलो' in query:
            speak("गूगल खोला जा रहा है")
            webbrowser.open("google.com")
        elif 'समय' in query or ' टाइम' in query :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'समय हो रहा है {strtime}')
            
        elif 'आप कैसे हैं' in query or 'कैसे हो' in query:
            speak("मैं ठीक हूँ, धन्यवाद")
            speak("आप कैसे है")
                
        elif 'ठीक' in query or "अच्छा" in query:
            speak("यह जानकर अच्छा लगा कि आप ठीक हैं")
			
        elif 'एग्जिट' in query or "बंद करो" in query:
            speak("मुझे अपना समय देने के लिए धन्यवाद")
            exit()
        elif 'आरजीयू वेबसाइट' in query or 'राजीव गांधी की वेबसाइट' in query :
            speak("आरजीयू वेबसाइट खोला जा रहा है")
            webbrowser.open("https://rgu.ac.in/")

        elif 'एडमिशन' in query or 'एडमिशन पोर्टल खोलो' in query :
            speak("आरजीयू का एडमिशन पैनल खोला जा रहा है")
            webbrowser.open("https://admissions.rgu.ac.in/") 

        elif 'विकिपीडिया' in query or 'सर्च ' in query:
            speak('विकिपीडिया में खोजा जा रहा है।...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("विकिपीडिया के अनुसार...")
            print(results)
            say(results)

        elif 'यूट्यूब' in query:
                speak('आप यूट्यूब पर क्या खेलना चाहते हैं..')
                video = takeCommand_hi().lower()
                speak('यहां आप अपनी क्वेरी के साथ यूट्यूब पर जा रहे हैं')
                kit.playonyt(video)

        elif 'गूगल' in query:
                speak('आप गूगल पर क्या सर्च करना चाहते हैं...')
                query = takeCommand_hi().lower()
                speak('यहां आप अपनी क्वेरी के साथ गूगल पर जा रहे हैं')
                kit.search(query)

        elif "बनाया" in query or "इस दुनिया में" in query or "तुम कैसे बने" in query :
                speak("मैं प्रवीण द्वारा बनाया गया हू, और बाकी एक रहस्य है ")
        
        elif "नमस्ते" in query or "हाय साथी" in query:
               speak("जी, मैं आपका मदद कैसे कर सकता हूँ")
