
import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import dirs
import pyjokes
from selenium import webdriver  #chrome external window
import time
import requests  #for weather
import subprocess  #all internal exe file
from datetime import date
import calendar
import pytz  #pip install pytz


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

speed=engine.getProperty('rate')
engine.setProperty('rate',150)


Browser_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe %s'
cdriver = 'C:\\Users\\Mr.nitish yadav\\Downloads\\BraveBrowserSetup.exe'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("\n \t\t--> Let's Go \n")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning !, Sir...\n")
        speak("Good Morning, Sir")

    elif hour >= 12 and hour < 18:
        print("Good Afternoon!, Sir.. \n")
        speak("Good Afternoon, Sir.. ")

    else:
        print("Good Evening!, Sir...\n")
        speak("Good Evening, Sir")

    print(
        "I am YADAV, The AI Assistant of Mr.nitish yadav ... How can i help you...!  "
    )
    speak(
        "I am  YADAV, The AI Assistant of, Nitish yadav... How can i help you...!  "
    )


def takeCommand():
    #It takes microphone input from the user and returns output as text

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n Listening...\n")
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 0.5)
        audio = r.listen(source)

    try:
        print("\n Understandind...\n")
        command= r.recognize_google(audio, language='en-in')
        print(f"Your command : {command}\n")

    except Exception as e:
        # print(e)
        print("come again please...")
        return "None"
    return command


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('21cs120@kpriet.ac.in','yadav123')
    server.sendmail('21cs120@kpriet.ac.in', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    cmd = 1
    while cmd:

        command = takeCommand().lower()

        # Logic for executing tasks based on user command
        
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            command = command.replace("search", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif (('quit' in command) or ('exit' in command) or ('stop' in command)
              or ('good night' in command)):
            if 'good night' in command:
                hour = int(datetime.datetime.now().hour)
                if ((hour >= 21 and hour < 24) or (hour >= 0 and hour <= 2)):
                    speak(
                        "Ok sir, Good Night.. I am always with you sir, bye, Take care.."
                    )
                    cmd = 0
                else:
                    speak("No sir.. Dont make me a fool... ")
            else:
                speak("Ok sir.. i hope, i did well, bye sir, Take care..")
                cmd = 0
        elif (('good morning' in command) or ('good afternoon' in command)
              or ('good evening' in command)):

            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")

            elif hour >= 12 and hour < 18:
                print("Good Afternoon! sir...")
                speak("Good Afternoon! sir...")
            elif hour >= 18 and hour < 24:
                print("Good evening sir..")
                speak("Good evening sir..")
        
        elif "tired" in command or "feeling tired" in command:
            s=" ok sir!. playing your favorite song"
            speak(s)
            kit.playonyt("https://www.youtube.com/watch?v=Aag8lBwCBK0")
            cmd=0

        elif "who is" in command or "what is" in command:
            search=command.replace("who is","")
            search=command.replace("what is","")
            info=wikipedia.summary(search,1)
            print(info)
            speak("accourding to wikipedia"+info)

        elif  (('show me' in command) or ('where am i' in command) or ('location' in command) or ('locate me' in command)):
            speak(" sure sir. opening map ")
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.open(url)
            speak("Here is the current location on your screen")
            #open_web("https://www.google.com/maps/search/?api=1&" + location + "")

        
        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif "how are you" in command:
            print("i am fine sir. thank you. tell me what can i do for you")
            speak("i am fine sir. thank you. tell me what can i do for you")  


        elif "hello" in command or "hey" in command:
            print("Hello sir.How can i help you")
            speak("Hello sir.How can i help you")         

        elif 'play' in command or 'youtube' in command:

            command = command.replace("play", "")
            command = command.replace("search", "")
            kit.playonyt(command)
            print(f"playing, {command}")
            speak(f"playing, {command}")

        elif 'open google' in command:
            print("opening google....")
            speak("opening google....")
            url = "google.com"
            #chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.get().open(url)
            
        # Portfolio function start
        elif 'portfolio' in command:
            print("opening portfolio website....")
            speak("opening the Boss portfolio  ....")
            url="https://yadavnitish.netlify.app/"
            webbrowser.get().open(url)
            speak("What's the next command for me sir ")


        # Portfolio function end
        elif 'google' in command or 'search' in command:
            command = command.replace("in","")
            command = command.replace("on","")
            command = command.replace("google","")
            command=command.replace("search","")
            tab = "http://google.com/?#q="
            webbrowser.open(tab+command)
            speak("Result on your screen sir")
            speak("tell me the next command")
                

        elif 'open gmail' in command:
            speak("ok sir, opening gmail")
            webbrowser.open("www.gmail.com")
            speak("Gmail on your screen, Sir...")
            speak("tell me the next command")

        elif 'open facebook' in command:
            print("opening facebook....")
            speak("opening facebook....")
            #url = 'www.facebook.com'
            webbrowser.open('www.facebook.com')
            speak("Facebook on your screen, Sir...")
            speak("tell me the next command")

        elif 'open whatsapp' in command:
            # webbrowser.open("www.whatsappweb.com")
            print("opening whatsapp....")
            speak("opening whatsapp....")
            #url = 'web.whatsapp.com'
            webbrowser.open('web.whatsapp.com')
            speak("Whatsapp on your screen, Sir...")
            speak("tell me the next command")

        elif 'show my last' in command:
            file = open("pywhatkit_dbs.txt", "r", encoding='utf-8')
            content = file.read()
            file.close()
            if content == "--------------------":
                content = None
            print(content)
            speak(content)

        elif 'open control' in command:
            print("opening Control panel....")
            speak("opening Control panel....")
            subprocess.call('control.exe')
            speak("Control Panel on your screen, Sir...")
            speak("tell me the next command")


        elif 'open file' in command:
            speak("Opening File Explorer")
            subprocess.call('explorer.exe')
            speak("File explorer on your screen, Sir...")
            speak("tell me the next command")

        elif (('music' in command) or ('gana' in command)):
            music_dir = 'E:\\VIDEO songs'
            songs = os.listdir(music_dir)
            print("Ok Sir, Playing music....")
            speak("ok Sir, Playing music....")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))
            speak("Ready to take next command")

        elif "time" in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time is {strTime}")
            speak(f" the time is {strTime}")
            speak("what's next sir")

        elif (('open visual studio' in command) or ('open vs code' in command)):
            speak("Opening VS code Application")
            codePath = "C:\\Users\\SBK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opened vs code on your screen sir..")

        elif ('about' in command):
            print(
                'Hello sir, My name is Yadav, Developed By Nitish Yadav. and i am Virtual Voice Assitant. tell me how can i assist you'
            )
            speak(
                'Hello sir, My name is Yadav, Developed By Nitish Yadav. and i am Virtual Voice Assitant. tell me how can i assist you'
            )

        elif 'date' in command:
            today = datetime.datetime.now()
            today1 = today.strftime("%d, %B, ")
            rr = str(today.year)
            today1 = today1 + rr
            print("Today date is.")
            print(today1)
            speak("today date is.")

            speak(today1)

            speak("Next Command sir")

        elif 'today' in command:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                print("Good Morning! sir...")
                speak("Good Morning! sir...")
            elif hour >= 12 and hour < 18:
                print("Good Afternoon! sir...")
                speak("Good Afternoon! sir...")
            elif hour >= 18 and hour < 24:
                print("Good evening sir..")
                speak("Good evening sir..")
            today = datetime.datetime.now()
            today1 = today.strftime("%d, %B, ")
            rr = str(today.year)
            today1 = today1 + rr
            print("today date is...", today1)
            speak("today date is..." + today1)
            date = date.today()
            st = calendar.day_name[date.weekday()]
            print("today is, ", st)
            speak("today is, " + st)
        elif 'day' in command:

            date = date.today()
            st = calendar.day_name[date.weekday()]
            speak("today is, " + st)
            print("today is, ", st)

            speak("Ready for next command sir")

        elif 'send email' in command or 'send a mail' in command:
            try:
                speak("sure sir, Give the Name of Reciever.")
                so = to = takeCommand()
                dic = {
                    "pratik": "21cs195@kpriet.ac.in",
                    
                    "Nitish": "mr.nitish8752@gmail.com",

                    "Niteesh": "mr.nitish8752@gmail.com",

                    "Diwakar": "ds6228353@gmail.com",
                  
                    "jay": "21cs192@kpriet.ac.in",
                  
                    "Bikki": "21cs191@kpriet.ac.in",
                    "Pranesh": "21cs128@kpriet.ac.in"
                }

                #so = to = takeCommand()
                to = dic[to]
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak(f"Email has been sent! to ,{so}, Thankyou....")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

                speak("Give me the Next Command")

        elif (('who are you' in command) or ('your name' in command)):
            print('I am AI Based Yadav,. i am assistant of Nitish Yadav...  ')
            speak('I am AI Based Yadav,. i am assistant of,  Nitish yadav....  ')
            speak("what can i do for you")

        elif 'favourite song' in command:
            speak("my favroit song is, Amplifier.. Do you want to play")
            command = takeCommand().lower()
            if (('yes' in command) or ('yah' in command)):
                url = 'https://www.youtube.com/watch?v=r9h1_33jUCk'
                speak("Playing My Favorite song")
                webbrowser.get(Browser_path).open(url)
                cmd=0
            else:
                speak("ok sir, no problem")

        elif 'open github' in command:
            print('opening Github profile')
            speak("opening Github ")
            webbrowser.open('https://github.com/Mr-nitish')
            speak("Your Github on your screen sir ")
            speak("What's next sir")

        elif 'whatsapp' in command or 'message on whatsappp' in command:
            try:
                print("Give the name of reciever")
                speak("Give the name of reciever")
                di = {
                    "jay": "+918431038986",
                    "pratik": "+919931842524",
                    "Bikki": "+918146034165",
                    "Pranesh": "+916366078153"
                }
                number = di[takeCommand()]

                print("What message you want to send.")
                speak("What message you want to send.")
                whatmsg = takeCommand()
                print("Time in hour.")
                speak("Time in hour.")
                hour = int(takeCommand())
                print(hour)
                print("Time in minute.")
                speak("Time in minute.")
                minu = int(takeCommand())
                print(minu)
                kit.sendwhatmsg(number, whatmsg, hour, minu)
                speak("Done sir what's the next command for me ")

            except Exception as e:
                print(e)
                speak(
                    "Sorry Sir. I am not able to send this...     Try again..")

        elif 'close music' in command:
            os.system('taskkill /f /im vlc.exe')
            speak("Done sir , Next please")
        elif 'close file' in command:
            os.system('taskkill /f /im explorer.exe')
            speak("Done sir , Next please")
        elif 'close chrome' in command:
            os.system('taskkill /f /im chrome.exe')
            speak("Done sir , Next please")

        elif 'turn off pc' in command:
            speak("When pc will turning off..Give time in second..")
            shut = int(takeCommand())
            shuts = str(shut)
            os.system('shutdown -s -t ' + shuts)
            print("pc will turning off in ", shuts, " second..")
            speak("pc will turning off in " + shuts + " second..")
            speak("Thank for using me, have a great day")

        elif 'cancel' in command:
            cont = "shutdown /a"
            os.system(cont)
            print("Ok sir,Dont worry I will not shut down your system")
            speak("Ok sir,Dont worry, I will not shut down your system")
        elif 'hello' in command:
            print("Hello sir, What can i do for you..")
            speak("hello sir, What can i do for you..")

        elif (("calculation" in command) or ("calculate" in command)):
            speak("ok sir. plz enter the operator")
            opr =input(" operator = ")

            speak(" now enter the two numbers : ")
            n1=int(input())
            n2=int(input())
            if opr == '+' or 'plus':
                r=n1+n2
                speak(" here is the result ")
                print(r)
            elif opr == '-' or 'minus':
                r=n1-n2
                speak(" here is the result ")
                print(r)
            elif opr == 'multiply' or 'x':
                r=n1*n2
                speak(" here is the result ")
                print(r)
            elif opr == 'divide' or '/':
                r=n1/n2
                speak(" here is the result ")
                print(r)
            elif opr == 'power' or '^':
                r=n1**n2
                speak(" here is the result ")
                print(r)
            else:
                speak("Wrong Operator")
            
            speak("Hope Perfomed successfully, Ready to take next command")

        elif 'weather' in command:
            try:
                api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=248932e95581539a55245ccabc4b8e65&q='
                unit = '&units=metric'
                speak("Tell me city name.")
                city = takeCommand()
                url = api_address + city + unit
                json_data = requests.get(url)

                data = json_data.json()
                temp = data['main']['temp']
                temp = str(temp)
                hum = data['main']['humidity']
                hum = str(hum)
                wind = data['wind']['speed']
                wind = wind * 2
                wind = str(wind)
                vis = data['visibility']
                vis = vis / 100
                vis = str(vis)
                discript = data['weather'][0]['main']
                discript = str(discript)

                print("tempreature is ", temp, " degree celcius..")
                speak("tempreature is " + temp + " degree celcius..")

                print("Humidity is ", hum, " percent..")
                speak("Humidity is " + hum + " percent..")

                print("Speed of wind is ", wind, " miles per hour..")
                speak("Speed of wind is " + wind + " miles per hour..")

                print("Discription of Visibility is ", discript)
                speak("Discription of Visibility is " + discript)

                print(" Visibility is ", vis, " metre..")
                speak(" Visibility is " + vis + " metre..")

                speak("Next command for me sir ")
            except Exception as e:
                print("")
                speak(
                    "Sorry Sir. I am not able to Give you Report, please Try again..")
        
                print("")
                speak(
                    "Sorry Sir. I am not able to Give you Report, Try again..")


