import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Voice / Language options
id1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"


# Hear the microphone and return the audio as text
def transform_audio_into_text():

    # store recognizer in variable
    r = sr.Recognizer()

    # set microphone
    with sr.Microphone() as source:

        # waiting time
        r.pause_threshold = 0.8

        # report that recording has begun
        print("You can now speak")

        # save what you hear as audio
        audio = r.listen(source)

        try:
            # search on google
            request = r.recognize_google(audio, language="en-gb")

            # test in text
            print("You said " + request)

            # return request
            return request

        # in case it does not understand audio
        except sr.UnknownValueError:

            # show proof that it did not understand the audio
            print("Ups! I did not understand audio")

            # return error
            return "I am still waiting"

        # In case the request cannot be resolved
        except sr.RequestError:

            # show proof that it did not understand the audio
            print("Ups! there is no service")

            # return error
            return "I am still waiting"

        # Unexpected error
        except:

            # show proof that it did not understand the audio
            print("Ups! something went wrong")

            # return error
            return "I am still waiting"

# Function so the assistant can be heard
def speak(message):

    # start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id2)

    # deliver message
    engine.say(message)
    engine.runAndWait()

# Inform day of the week
def ask_day():

    # Create a variable with today information
    day = datetime.date.today()
    # print(day)

    # Create variable for day of the week
    week_day = day.weekday()
    # print(week_day)

    # Names of days
    calendar = {0: "Monday",
                1: "Tuesday",
                2: "Wednesday",
                3: "Thursday",
                4: "Friday",
                5: "Saturday",
                6: "Sunday"}

    # Say the day of the week
    speak(f'Today is {calendar[week_day]}')

# Inform what time it is
def ask_time():

    # Variable with time information
    time = datetime.datetime.now()
    time = f"At this moment, it is {time.hour} hours and {time.minute} minutes"
    # print(time)

    # Say the time
    speak(time)

# Create initial greeting
def initial_greeting():

    # Say greeting
    speak("Hello, I am Zira. How can I help you?")

# Main function of the assistant
def vir_assistant():

    # Activate the initial greeting
    initial_greeting()

    # Cut-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        vir_request = transform_audio_into_text().lower()

        if "open youtube" in vir_request:
            speak("Sure, I am opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "open browser" in vir_request:
            speak("Of course, I am on it")
            webbrowser.open("https://www.google.com")
            continue
        elif "What day is today" in vir_request:
            ask_time()
            continue
        elif "do a wikipedia search for" in vir_request:
            speak("I am looking for it")
            vir_request = vir_request.replace("do a wikipedia search for", "")
            answer = wikipedia.summary(vir_request, sentences=1)
            speak("according to wikipedia: ")
            speak(answer)
            continue
        elif "search the internet for" in vir_request:
            speak("Of course, right now")
            vir_request = vir_request.replace("search the internet for", "")
            pywhatkit.search(vir_request)
            speak("this is what I found")
            continue
        elif "play" in vir_request:
            speak("oh, what a great idea! I'll play it right now")
            pywhatkit.playonyt(vir_request)
            continue
        elif "joke" in vir_request:
            speak(pyjokes.get_joke())
            continue
        elif "stock price" in vir_request:
            share = vir_request.split()[-2].strip()
            portfolio = {"apple": "APPL",
                         "amazon": "AMZN",
                         "google": "GOOGL"}
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info["regularMarketPrice"]
                speak(f"I found it! The price of {share} is {price}")
                continue
            except:
                speak("I am sorry, but I did not find it")
                continue
        elif "goodbye" in vir_request:
            speak("I am going to rest. Let me know if you need anything")
            break

vir_assistant()