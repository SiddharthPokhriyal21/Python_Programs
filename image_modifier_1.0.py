import cv2
import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    print("Welcome to Image Modifier 1.0")
    engine.say("Welcome to Image Modifier 1.0")
    engine.runAndWait()

    while True:
        print("What do you want to do?")
        engine.say("What do you want to do?")
        engine.runAndWait()
        x = int(input("Enter 1 for Image Resizing.\nEnter 2 for Image Quality Enhancement.\nEnter 0 to exit.\n"))

        if x == 0:
            print('Thank you!')
            engine.say('Thank you!')
            engine.runAndWait()
            break

        elif x == 1:
            src = input("Enter the source path: ")
            original_image = cv2.imread(src, cv2.IMREAD_UNCHANGED)

            scale_percent = int(input("Enter the percentage size: "))

            new_height = int(original_image.shape[0]*scale_percent/100)
            new_width = int(original_image.shape[1]*scale_percent/100)

            output = cv2.resize(original_image, (new_width, new_height))

            dest = input("Enter the destination path: ")
            cv2.imwrite(dest, output)
        
        elif x == 2:
            src = input("Enter the source path: ")
            original_image = cv2.imread(src, cv2.IMREAD_UNCHANGED)

            while True:
                y = int(input("Press 1 for image smoothening.\nPress 2 to enhance image contrast.\nPress 0 to get the image.\n"))

                if y == 0:
                    break

                elif y == 1:
                    smooth = int(input("Enter the smoothening index: "))
                    output = cv2.detailEnhance(original_image, sigma_s = smooth)

                elif y == 2:
                    contrast = int(input("Enter the percentage contrast: "))
                    output = cv2.detailEnhance(original_image, sigma_r = contrast)

                else:
                    print("Kindly try a valid input.")
                    engine.say("Kindly try a valid input.")
                    engine.runAndWait()

            dest = input("Enter the destination path: ")
            cv2.imwrite(dest, output)

        else:
            print("Kindly try a valid input.")
            engine.say("Kindly try a valid input.")
            engine.runAndWait()