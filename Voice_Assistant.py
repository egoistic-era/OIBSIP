import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

# Text-to-speech setup
voice_engine = pyttsx3.init()

def speak_output(message):
    print("Assistant:", message)
    voice_engine.say(message)
    voice_engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("Please speak...")
        recognizer.adjust_for_ambient_noise(mic)
        audio_data = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text.lower()
    except:
        speak_output("Could not understand, please try again.")
        return ""

def assistant():
    speak_output("Hi! I am your personal assistant.")

    running = True
    while running:
        user_input = get_voice_input()

        if not user_input:
            continue

        if "hi" in user_input or "hello" in user_input:
            speak_output("Hello there!")

        elif "what time" in user_input or "time" in user_input:
            current_time = datetime.now().strftime("%I:%M %p")
            speak_output(f"The time is {current_time}")

        elif "date" in user_input or "today" in user_input:
            today_date = datetime.now().strftime("%d %B %Y")
            speak_output(f"Today's date is {today_date}")

        elif "search" in user_input:
            speak_output("Tell me what you want to search")
            search_query = get_voice_input()
            if search_query:
                webbrowser.open("https://www.google.com/search?q=" + search_query)

        elif "bye" in user_input or "exit" in user_input:
            speak_output("Shutting down. Have a nice day!")
            running = False

        else:
            speak_output("Sorry, I can only help with basic tasks.")

# Start assistant
assistant()
