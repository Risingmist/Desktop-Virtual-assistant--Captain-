# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Desktop AI")

import datetime
import os
import random
import webbrowser as wb

import pyautogui
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pyttsx3
import speech_recognition as sr
import wikipedia
#import smtplib
import pyjokes

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def wish():
    print("Welcome back ma'am!!")
    speak("Welcome back ma'am!!")
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning ma'am!!")
        print("Good Morning ma'am!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ma'am!!")
        print("Good Afternoon ma'am!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening ma'am!!")
        print("Good Evening ma'am!!")
    else:
        speak("Good Night ma'am, See You Tommorrow")

    speak("Captain at your service ma'am, please tell me how may I help you.")
    print("Captain at your service ma'am, please tell me how may I help you.")

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The date today  is")
    speak(day)
    speak(month)
    speak(year)
    print("The date is " + str(day) + "/" + str(month) + "/" + str(year))



def screenshot():
    img = pyautogui.screenshot()
    img.save(r"C:\Users\shrey\OneDrive\Desktop\img\jarvis.jpg")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm Captain and I'm a desktop voice assistant.")
            print("I'm Captain  and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine ma'am, What about you?")
            print("I'm fine ma'am, What about you?")

        elif "fine" in query:
            speak("Glad to hear that ma'am!!")
            print("Glad to hear that ma'am!!")

        elif "good" in query:
            speak("Happy to hear that ma'am!!")
            print("Happy to hear that ma'am!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait ma'am, I'm searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page ma'am, please ask something else")

        elif "open flipkart" in query:
            wb.open("https://www.flipkart.com")
            speak("Opening flipkart ma'am")

        elif "open snapdeal" in query:
            wb.open("https://www.snapdeal.com")
            speak("Opening snapdeal ma'am ")

        elif "open amazon" in query or 'shop online' in query:
            wb.open("https://www.amazon.com")
            speak("Opening amazon ma'am ")

        elif "open yahoo" in query:
            wb.open("https://www.yahoo.com")
            speak("Opening yahoo ma'am ")

        elif "open github" in query:
            wb.open("https://www.github.com")
            speak("Opening github ma'am ")

        elif "open instagram" in query:
            wb.open("https://www.instagram.com")
            speak("Opening instagram ma'am")

        elif "open facebook" in query:
            wb.open("https://www.facebook.com")
            speak("Opening facebook  ma'am")

        elif "open youtube" in query:
            wb.open("youtube.com")

        elif "open google" in query:
            wb.open("google.com")

        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            song_dir = r"C:\Users\shrey\OneDrive\Desktop\music"
            songs = os.listdir(song_dir)
            print(songs)
            x = len(songs)
            y = random.randint(0, x)
            os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")


        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))

        elif "screenshot" in query:
            screenshot()
            speak("Screenshot taken, please check it")


        elif "offline" in query:
            quit()

