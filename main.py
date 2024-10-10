import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
#pip install pocketsphinx
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

if __name__== "__main__":
    speak("Initializing jarvis.....")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()


        print("recognizing")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=4,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source,timeout=4,phrase_time_limit=2)
                    command = r.recognize_google(audio)

                processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
