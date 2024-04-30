import requests
import pyttsx3
import json
import openai

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
        print("Enter 1 to use specific keywords.\nEnter 0 to exit.")
        x = int(input())

        if x == 0:
            print("Thank you!")
            speaker.say("Thank you!")
            speaker.runAndWait()
            break

        elif x == 1:
            key = input("Enter the keywords: ")
            url = f"https://newsapi.org/v2/everything?q={key}&apiKey=65edd986632648b0a6720e12f758f4d4"
            r = requests.get(url)
            w_dict = json.loads(r.text)

        else:
            print("Kindly try a valid input.")
            speaker.say("Kindly try a valid input.")
            speaker.runAndWait()

        print(f"Headlines related to {key} are as follows: ")
        for i in range(w_dict["totalResults"]):
            headline = w_dict["articles"][i]["title"]
            print(f"{headline}\nDo you wish to ellaborate on the headline?")
            x = int(input("Enter 1 for yes and 2 for no.\nEnter 0 to go back.\n"))
            if x == 1:
                openai.api_key = "sk-proj-9ALXEfVlHrzLDTSLiv6MT3BlbkFJldgCEgAS5kHcL45Qd7Ev"
                content = w_dict["articles"][i]["url"]
                prompt = f"Summarize the given news for me in a paragraph.\n{content}"
                messages = []
                message = f"Provide a precis on the news article in the given URL: {content}"
                messages.append({"role": "user", "content": message})
                response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print('\n' + reply + '\n')
                speaker.say(reply)
                speaker.runAndWait()
            
            elif x == 2:
                continue
            
            elif x == 0:
                break

            else:
                print("Kindly try a valid input.")