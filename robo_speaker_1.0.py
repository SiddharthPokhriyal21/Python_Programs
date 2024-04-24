import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to the Robo Speaker 1.0")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    while True:
        x = input("Enter what you want to say: ")
        if x == 'q':
            engine.say('Bye Bye!')
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
