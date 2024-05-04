import pyttsx3
from pydub import AudioSegment


if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    print("Welcome to Audio Modifier 1.0")
    engine.say("Welcome to Audio Modifier 1.0")
    engine.runAndWait()

    while True:
        print("What do you want to do?")
        engine.say("What do you want to do?")
        engine.runAndWait()
        x = int(input("Enter 1 to convert a normal audio to an 8D audio. (UNDER PROGRESS)\nEnter 0 to exit.\n"))

        if x == 0:
            print('Thank you!')
            engine.say('Thank you!')
            engine.runAndWait()
            break

        # elif x == 1:
        #     audio_files = []
        #     while True:
        #         path = input("Enter the source path: ")
        #         if path == '?':
        #             break
        #         audio_files.append(path)

        #     for file_name in audio_files:
        #         audio = AudioSegment.from_file(file_name, format="wav")

        #         # Apply spatial effects (e.g., panning, delay)
        #         # Implement your spatial audio processing techniques here

        #         channel1 = audio.pan(-1)
        #         channel2 = audio.pan(1)

        #         combined = channel1.overlay(channel2)

        #         combined.export(f"{file_name}_8D_audio.wav", format="wav")

        else:
            print("Kindly try a valid input.")
            engine.say("Kindly try a valid input.")
            engine.runAndWait()