# import speech_recognition as sr
# import pyttsx3
# recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Listening...")
#     audio = recognizer.listen(source)  # Captures my  voice as per i used lib

# command = recognizer.recognize_google(audio)
# command = command.lower()  # Convert to lowercase for easy matching
# import datetime
# if "time" in command:
#     current_time = datetime.datetime.now().strftime("%I:%M %p")  
#     print("Current time is:", current_time)

# import webbrowser
# if "open youtube" in command:
#     webbrowser.open("https://www.youtube.com")


# if "exit" in command or "stop" in command:
#     print("Goodbye!")
#     exit()
# try:
#     command = recognizer.recognize_google(audio)
#     command = command.lower()
#     print("You said:", command) 
# except sr.UnknownValueError:
#     print("Sorry, I couldn't understand what you said.")
#     exit()
# except sr.RequestError:
#     print("Could not connect to the speech recognition service.")
#     exit()


import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    try:
        audio = recognizer.listen(source)  # Captures your voice
        command = recognizer.recognize_google(audio)
        command = command.lower()  # Convert to lowercase for easy matching
        print("You said:", command)  # Print recognized text

        # Process commands
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")  # Get time in HH:MM AM/PM format
            print("Current time is:", current_time)

        elif "open google please" in command:
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command or "stop" in command:
            print("Goodbye!")
            exit()

        else:
            print("I didn't understand that.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        print("Could not connect to the speech recognition service.")
