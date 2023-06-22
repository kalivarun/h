import pyttsx3
speech = pyttsx3.init()
ans = input('enter text : ')
speech.say(ans)

var = " hello this is a test to check the voice of the program 1 2 3 4 5 6 nee pellii    fix"
speech.say(var)
speech.runAndWait()
