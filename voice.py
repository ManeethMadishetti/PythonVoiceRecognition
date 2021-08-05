import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice',voices[1].id)
  
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi Maneeth . I am Your Assistant sir. Please tell me how may i help you")

def takeCommand():
    #takes mike input and return string op
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....Speak Now")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print("User said:",query)
        speak(query)
        
    except Exception as e:
        print(e)

        print("Say That agian Please...")
        return "None"
    return query
def sendEmail(to,content):

  #  server=smtplib.SMTP('smtp.gmail.com',587)
  #  server.ehlo()
   # server.starttls()
  #  server.login('javacode2428@gmail.com','Badri2428')
 #   server.sendmail('maneethsai1509@gmail.com',to,content)
#    server.close()

    sender = 'javacode2428@gmail.com'
    receivers = ['maneethsai1509@gmail.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)         
        print ("Successfully sent email")
    except SMTPException:
        print ("Error: unable to send email")

def main():
    wishMe()
    while True:
        query=takeCommand().lower()
         #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir="E:\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'wynk' in query:
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe --profile-directory=Default --app-id=emacdpakoihlgkpbekbfnhinbipjbepd")
        elif 'the time' in query:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{t}")
        elif 'open code' in query:
            codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("What do you want to send ")
                content=takeCommand()
                to="maneethsai1509@gmail.com"
                sendEmail(to,content)
                speak("email sent")
            except Exception as e:
                print(e)
                speak("sorry maneeth i cant send mail at these moment")
        elif 'exit' in query:
            speak('i think you enjoyed ....')
            break
main()