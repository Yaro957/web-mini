
import pyttsx3

print("welcome to Robospeaker 1.1 created by Lucifer")
text_speech = pyttsx3.init()
while(True):
    x=input("what do you wnat me to speak?\n")
    text_speech.setProperty('rate',100)
    # voices=text_speech.getProperty('voices')
    # text_speech.setProperty('voice',voices[1].id)
    text_speech.say(x)
    text_speech.runAndWait()
    # rate=text_speech.getProperty('rate')
    # print(rate)
    