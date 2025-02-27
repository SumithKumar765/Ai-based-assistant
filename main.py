import pyttsx3
from plyer import notification
import pyautogui
import speech_recognition as sr #import speech recgonisation part 
import random

import webbrowser
import wikipedia
import datetime
import pywhatkit as pwk




engine = pyttsx3.init() 
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
engine.setProperty("rate",170)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def command():
    content = " "
    while content == " ":
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

            # recognize speech using Google Speech Recognition
        try:
            content = r.recognize_google(audio, language='en-in')
            print("you said ........." + content)
        except Exception as e:
            speak("i did not understand can pleaase tell agin!")
            print("please try agin i did'nt get you")
    return content
def main_process():
    while True:
        request= command().lower()
        if "hello" in request:
           speak("HI , this is jarvis How can i help you")
        elif "open google" in request:
            speak("opening google")
            webbrowser.open("https://www.google.co.in")
        elif "open gmail" in request:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "play music" in request:
            speak("playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=qaf4cDPsW68")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=rYnobU1dtUU")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=rYnobU1dtUU")
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("current time is "+ str(now_time) )
        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d:%m")
            speak("current date is "+ str(now_date) )
        elif "new task" in request:
            task = request.replace("new task","")
            task = task.strip()
            if task != "":
                speak("Adding task: "+ task)
                with open ("todo.txt","a") as file:
                    file.write(task + "\n")
        elif "what are today tasks" in request:
             with open ("todo.txt","r") as file:
                 speak("work we have to do today is :"+ file.read())
        elif"show work" in request:
            with open ("todo.txt","r") as file:
                 tasks = file.read()
                 notification.notify(
                     title="todays work",
                     message = tasks    
                 )
        elif"open youtube" in request:
            webbrowser.open("www.youtube.com")
        elif"open linkdin" in request:
            webbrowser.open("https://in.linkedin.com/")
        elif"open whatsapp" in request:
            webbrowser.open("https://web.whatsapp.com/")       
        elif"open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif"wikipedia" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search  on wikipedia", "")
            result = wikipedia.summary(request, sentences=5)
            print(result)
            speak(result)
        elif"search on google" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search   google", "")
            webbrowser.open("https://www.google.com/search?q="+request )    
         
        elif"send whatsappmessage" in request:
            # Send a WhatsApp Message to a Contact at 2:30 PM
            pwk.sendwhatmsg("7659833962", "Happy birth day", 14, 30, 60)
        elif"shutdown" in request:
           pwk.shutdown ( 30) 
           
        elif" cancel shutdown" in request:
          pwk.cancel_shutdown()
        
        
    
        
        
        




           
main_process()
