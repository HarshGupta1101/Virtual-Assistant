import pyttsx3
import speech_recognition as sr
import datetime
import os
import wolframalpha
import wikipedia
import webbrowser
import pywhatkit
import cv2
#import pyscreenshot 
import pyautogui
import smtplib
from email.message import EmailMessage
import time
from playsound import playsound
import pyjokes
from PyQt5.QtCore import QTimer, QTime, QDate ,Qt,QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from file2 import Ui_MainWindow
import requests
import sys


engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):    
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    assistant_name =("Selina")
    speak("I am your Assistant")
    speak(assistant_name)

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising ....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice .")
        return "None"
    return query

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        #print("The Set Date is:",date)
        #print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            p = multiprocessing.Process(target=playsound, args=("alarm_beeps.mp3",))
            p.start()
            #input("press ENTER to stop playback")
            #time.sleep(5)
            while True:
                if keyboard.is_pressed("q"): #If Q key is pressed
                    p.terminate()
                    break
            #playsound.playsound("alarm_beeps.mp3")
            break

def sleep_wake():
    speak("OK sir")
    
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold=1
            audio=r.listen(source)
        try:
            query = r.recognize_google(audio,language='en-in').lower()
            print(f"User said : {query}\n")
            if "wake up" in query:
                speak("ok sir, I am ready for your service")
                break
        except Exception as e:
            print(e)

def takecommand1(in_lang):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening .... ")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising ....")
        query = r.recognize_google(audio,language=in_lang)
        
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice .")
        return "None"
    return query
            

def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vitminiproj@gmail.com', 'vit@mini@pro')
    email=EmailMessage()
    email['From']='vitminiproj@gmail.com'
    email['To']=to
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email)
    server.close()
      
def screenshot():
    img=pyautogui.screenshot()
    speak("With what name you would like save your screenshot")
    file_name=takecommand().lower()
    print(file_name)
    img.save(file_name+".jpg") 
    speak("Your screenshot is saved as "+file_name+".jpg")

    
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():

    year=(datetime.datetime.now().year)
    month=(datetime.datetime.now().month)
    date=(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def username():
    speak("What should i call you sir")
    uname = takecommand()
    speak("Welcome Mister")
    speak(uname)
    print("#####################")
    print("Welcome Mr.",uname)
    print("#####################")
     
    speak("How can i Help you, Sir")

def news():
    api_key="88ba967c3c80458481537769fd8386f1"
    main_url="https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news=requests.get(main_url).json()
    #print(news)
    article=news["articles"]
    #print(article)
    news_article=[]
    for arti in article:
        news_article.append(arti['title'])
        #print(news_article)
    for i in range(5):
        print(news_article[i])
        speak(news_article[i])

def taskexecution():
    wish()
    username()
    while True:
        query=takecommand().lower()
        print(query)
        if "stop listening" in query:
            speak("as you say sir")
            break
        elif "sleep" in query:
            sleep_wake()
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia :")
            print(results)
            speak(results)
        elif "the time" in query:
            Time=datetime.datetime.now().strftime("%I:%M:%S")
            speak(Time)
        elif "the date" in query:
            date()
        elif "news" in query:
            news()
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
        elif 'play' in query:
           song=query.replace('play','')
           speak('playing '+song)
           pywhatkit.playonyt(song)
        elif "open camera" in query:
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("test")
            
            img_counter = 0
            
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
            
                k = cv2.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1
            
            cam.release()
            
            cv2.destroyAllWindows()
        
        elif "alarm" in query:            
            data=pyautogui.prompt(text='To set the alarm Enter the time in 24 hr format', title=' ALARM' , default='23:59:00')
            #print(data)
            alarm(data)
        elif "open notepad" in query :
            os.startfile("C:\\WINDOWS\\system32\\Notepad")
        elif query in ["powerpoint presentation" , "ppt" , "powerpoint"]:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PowerPoint")
        elif "open outlook" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/OutLook")
        elif  query in ["open word" , "ms word"]:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word")
        elif "open excel" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel")
        elif "open vs code" in query:
            os.startfile("C:/Users/mi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk")
        elif query in ["open cmd","open command prompt"]:
            os.startfile("C:Users/mi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt")
        elif "open excel" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel")
        elif "open excel" in query:
            os.startfile("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel")
        
        elif "volume up" in query:
            for i in range(5):
                pyautogui.press("volumeup")
        elif "volume down" in query:
            for i in range(5):
                pyautogui.press("volumedown")
        elif "volume" and "mute" in query:
            pyautogui.press("volumemute")
        elif "volume" and "unmute" in query:
            pyautogui.press("volumeunmute")
        elif "screenshot" in query:
                screenshot()
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'translator' in query:
            
            time_string = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
            
            print(time_string)
            
            #print(googletrans.LANGUAGES)
            engine = pyttsx3.init()
            voices=engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            
            
            language_dict={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
            
            speak("Your translator is ready to go")

            while True:   
                speak("Tell the language you want to translate from")
                in_lang_u=takecommand1('en-in').lower()
                if in_lang_u=='none' :
                    speak("Sorry I didn't understand Please tell again")
                    continue
                else:
                    break
            
            while True:   
                speak("Tell the language you want to translate to")
                out_lang_u=takecommand1('en-in').lower()
                if out_lang_u=='none' :
                    speak("Sorry I didn't understand Please tell again")
                    continue
                else:
                    break
            
            
            
            for i in language_dict:
                if language_dict[i]==in_lang_u:
                    in_lang=i
                if language_dict[i]==out_lang_u:
                    out_lang=i
                    
            
            #out_lang="fr"
            #in_lang="en-in"
            speak("Please tell you wnat to translate")
            text=takecommand1(in_lang)
            translator = googletrans.Translator()
            translated = translator.translate(text,dest=out_lang)
            print(translated.text)
            print(in_lang)
            print(out_lang)
            
            try:
                convert_audio =gtts.gTTS(translated.text,'com',out_lang)
                convert_audio.save(time_string+'.mp3')
                playsound.playsound(time_string+'.mp3')
            except Exception as e:
                print(e)
            
            
                        

        elif 'email to vit' in query:
            try:
                speak("What is your subject of email?")
                subject=takecommand()
                speak("What is your message?")
                content = takecommand()
                to = "vitminiproj@gmail.com"   
                sendEmail(to, subject, content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry! I am unable to send this email. Please try again after some time.")

        else: 
            client = wolframalpha.Client("8Y8VX4-WVTQ9KY95X")
            if "none" not in query:
                res = client.query(query)
                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")
            else:
                pass
           

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        taskexecution()
   
    

startExecution=MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)
        

    def startTask(self):
        self.gui.label1=QMovie("element_jarvis.gif")
        self.gui.label.setMovie(self.gui.label1)
        self.gui.label1.start() 
        startExecution.start()
      
guiapp=QApplication(sys.argv)
var=Main()
var.show()
sys.exit(guiapp.exec_())    