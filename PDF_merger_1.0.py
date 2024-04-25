import PyPDF2
import docx2pdf
import pyttsx3
from pptx import Presentation
from pyexcelerate import Workbook

if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    print("Welcome to PDF Modifier 1.0")
    engine.say("Welcome to PDF Modifier 1.0")
    engine.runAndWait()

    while True:
        print("What do you want to do?")
        engine.say("What do you want to do?")
        engine.runAndWait()
        x = int(input("Press 1 to merge PDFs.\nPress 2 to convert a Word file to a PDF.\nPress 3 to convert an PowerPoint presentation to a PDF. (Under progress)\nPress 4 to convert an Excel sheet to a PDF. (Under progress)\nPress 0 to exit.\n"))

        if x == 0:
            print('Thank you!')
            engine.say('Thank you!')
            engine.runAndWait()
            break

        elif x == 1:
            pdf_files = []
            while True:
                path = input("Enter the source path: ")
                if path == '?':
                    break
                pdf_files.append(path)

            merger = PyPDF2.PdfMerger()

            for file_name in pdf_files:
                pdf_file = open(file_name, 'rb')
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                merger.append(pdf_reader)
            pdf_file.close()

            dest = input("Enter the destination path: ")
            merger.write(dest)
        
        elif x == 2:
            word_files = []
            while True:
                path = input("Enter the source path: ")
                if path == '?':
                    break
                word_files.append(path)

            dest = input("Enter the destination path: ")
            for file in word_files:
                docx2pdf.convert(file, dest)

        # elif x == 3:
        #     powerpoint_files = []
        #     while True:
        #         path = input("Enter the source path: ")
        #         if path == '?':
        #             break
        #         powerpoint_files.append(path)

        #     dest = input("Enter the destination path: ")
        #     for file in powerpoint_files:
        #         ppt = Presentation(file)
        #         ppt.save(dest)

        # elif x == 4:
        #     excel_files = []
        #     while True:
        #         path = input("Enter the source path: ")
        #         if path == '?':
        #             break
        #         excel_files.append(path)

        #     dest = input("Enter the destination path: ")
        #     for file in excel_files:
        #         wb = Workbook()
        #         wb.read(file)
        #         wb.save(dest)

        else:
            print("Kindly try a valid input.")
            engine.say("Kindly try a valid input.")
            engine.runAndWait()

# Hello World