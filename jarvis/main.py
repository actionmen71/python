import pyttsx3
# a module to work with audio

engine= pyttsx3.init("sapi5")
# engine is a variable which stores the initialization of voice from windows
# this api from microsot let us use stimulated voices present in the windows os itself

voices= engine.getProperty("voices")
# to store voices property from the engine variable which is now storing voice pack
# from windows into variable named voices

print(voices[1].id)
print(voices[0].id)
# this will print the different voices available in windows to chose from that we want to use
# there are only 0 and 1 voices available in windows and if we take 2 as a value it will print error
# or out of range index which means there are no other voices available

engine.setProperty("voice", voices[0].id)
# here we are setting O as default voice which is David





# function to speak whatever is passed to the argument named audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__=="__main__":
    speak("krishna you are awesome!")