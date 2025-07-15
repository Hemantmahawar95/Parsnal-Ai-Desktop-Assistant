import os
import ctypes
import platform
import random
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime

# Initialize engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Take voice command
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        speak("Say that again please...")
        return "none"

# Open websites
def open_website(query):
    websites = [
        ["open youtube", "https://www.youtube.com", "Opening YouTube"],
        ["open google", "https://www.google.com", "Opening Google"],
        ["open github", "https://www.github.com", "Opening GitHub"]
    ]

    for keyword, url, message in websites:
        if keyword in query:
            webbrowser.open(url)
            speak(message)
            return
    speak("Sorry!")

# Play music
def play_music(music_dir):
    songs = os.listdir(music_dir)
    if not songs:
        speak("No music files found in the folder.")
        return
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))
    speak(f"Playing {song}")

# System operations
def shutdown():
    speak("Shutting down the system.")
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the system.")
    os.system("shutdown /r /t 1")

def sleep():
    speak("Putting the system to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# Main Assistant Logic
def start_assistant():
    speak("Hello")

    while True:
        query = take_command()

        if query == "none":
            continue

        if "what is the time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "what is the date" in query:
            date = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {date}")

        elif "play music" in query:
            music_folder = "F:\\Song\\panjabi song"
            play_music(music_folder)

        elif "open vs code" in query:
            os.system(r'"C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')

        elif "shutdown my laptop" in query:
            shutdown()

        elif "restart my laptop" in query:
            restart()

        elif "sleep my laptop" in query:
            sleep()

        else:
            open_website(query)

if __name__ == "__main__":
    start_assistant()

