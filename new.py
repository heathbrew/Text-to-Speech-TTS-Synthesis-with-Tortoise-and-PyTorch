import speech_recognition as sr

def main():
    sound = "Sadhgurump3.mp3"
    r =sr.Recognizer()
    with sr.AudioFile(sound) as source :
        r.adjust_for_ambient_noise(source)
        print("Convertng Audio File to Text ...")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
        except Exception as e:
            print(e)
def takeCommand():
    """
    It take microphone input from the user and return a
    string output
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)           
if __name__ == "__main__":
    main()