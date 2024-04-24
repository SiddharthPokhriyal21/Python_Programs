import pyttsx3
import requests
import json


if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    
    print("Welcome to the Weather App 1.0")
    engine.say("Welcome to the Weather App 1.0")
    engine.runAndWait()

    while True:
        city = input("Enter the name of the city: ")
        if city == '0':
            print('Thank you!')
            engine.say('Thank you!')
            engine.runAndWait()
            break

        url = f"http://api.weatherapi.com/v1/current.json?key=c475ab3b62c94345a0c175236242204&q={city}"
        r = requests.get(url)
        w_dict = json.loads(r.text)

        temp_celsius = w_dict["current"]["temp_c"]
        local_time = w_dict["location"]["localtime"]

        day_night = w_dict["current"]["is_day"]
        if day_night == 0:
            day_night = 'night'
        else:
            day_night = 'day'

        print(f"The current temperature in {city} is {temp_celsius} degree Celsius.")
        engine.say(f"The current temperature in {city} is {temp_celsius} degree Celsius.")

        print(f"The local time in {city} is {local_time}. It's {day_night} in {city}.")
        engine.say(f"The local time in {city} is {local_time}. It's {day_night} in {city}.")

        engine.runAndWait()