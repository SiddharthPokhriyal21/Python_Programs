import requests
import pyttsx3
import json

if __name__ == "__main__":
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices")
    speaker.setProperty("voice", voices[0].id)
    print("Welcome to the News App 1.0")
    speaker.say("Welcome to the News App 1.0")
    speaker.runAndWait()
    while True:
        print("What do you want to do?")
        speaker.say("What do you want to do?")
        speaker.runAndWait()
        print("Press 0 to exit.")
        x = int(input())

        if x == 0:
            print("Thank you!")
            speaker.say("Thank you!")
            speaker.runAndWait()
            break

        elif x == 1:
            url = f"https://newsapi.org/v2/everything?q={key}&apiKey=65edd986632648b0a6720e12f758f4d4"
            r = requests.get(url)
            w_dict = json.loads(r.text)
            

        else:
            print("Kindly try a valid input.")
            speaker.say("Kindly try a valid input.")
            speaker.runAndWait()