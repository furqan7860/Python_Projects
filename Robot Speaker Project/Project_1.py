import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Furqan Amjad")
    while True:

        x = input("Enter what you want me to speak: ")
        if (x=="q"):
            break
        # initialize the pyttsx3 engine
        engine = pyttsx3.init()

        # set the rate of speech
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate + 10)

        # speak the input string
        engine.say("Hello"+x)
        engine.runAndWait()
