import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice to female (index 1) if available
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# Speak text aloud
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Listen for command
def take_command():
    try:
        with sr.Microphone() as source:
            print('🎙️ Listening...')
            voice = listener.listen(source, timeout=5, phrase_time_limit=6)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f">> You said: {command}")
                return command
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError:
        print("❌ Could not request results from Google Speech Recognition service.")
    except Exception as e:
        print(f"❌ Error: {e}")
    return ""

# Run assistant logic
def run_alexa():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '').strip()
        info = wikipedia.summary(person, sentences=1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('Sorry, I have a headache.')

    elif 'are you single' in command:
        talk('I am in a relationship with WiFi.')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')

# Loop the assistant
if __name__ == "__main__":
    while True:
        run_alexa()
