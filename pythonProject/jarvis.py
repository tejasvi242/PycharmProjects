import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import ssl
import autopy
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
path = "c://Users//" + os.getlogin() + "//Desktop//ScreenShots//" + str(datetime.date.today())

try:
    os.makedirs(path)
except FileExistsError:
    pass


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I Am Jarvis , welcome in your service")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . . ")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=ssl.create_default_context())
    server.ehlo()
    server.login('tejasvipatil759@gmail.com', 'sachasvi@1215')
    server.sendmail('tejasvipatil759@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            print("Jarvis is searching Wikipedia, pls wait!")
            speak("Searching Wikipedia, Sir please wait")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia...")
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'who are you' in query:
            speak("I am Jarvis, How may I help you?, sir")


        elif 'open google' in query:
            print("User said: Open Google")
            speak("Sir, opening Google")
            webbrowser.open("google.com")


        elif 'take screenshots' in query:
            shot = autopy.bitmap.capture_screen()
            now = datetime.datetime.now()
            timenow = now.strftime("%H_%M_%S")
            path = "c://Users//" + os.getlogin() + "//Desktop//ScreenShots//" + str(datetime.date.today())
            try:
                shot.save(path + '//' + timenow + '.png')
            except FileNotFoundError:
                os.makedirs(path)
                shot.save(path + '//' + timenow + '.png')
            speak("taken")

        elif 'open youtube' in query:
            print("User said: Open YouTube")
            speak("Sir, opening youtube")
            webbrowser.open("youtube.com")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Tejasvi,The time is {strTime}")

        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Sachin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'email to tejasvi' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "tejasvipatil759@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry Tejasvi, I am not able to send this email at a moment")

        elif 'play music' in query:
            music_dir = 'E:\\savi'
            print("songs")
            os.startfile(os.path.join(music_dir, 'kalimba.mp3'))

        elif 'open image' in query:
            music_dir = 'E:\\savi'
            os.startfile(os.path.join(music_dir, 'Nature.jpg'))

        elif 'exit' in query:
            speak("Okk Thank you Bye Sir...")
            exit()

