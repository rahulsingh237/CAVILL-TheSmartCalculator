import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
def male(audio):
   engine.setProperty('voice',voices[0].id)
   engine.say(audio)
   engine.runAndWait()
   return -1

def female(audio):
   engine.setProperty('voice',voices[1].id)
   engine.say(audio)
   engine.runAndWait()
   return -1