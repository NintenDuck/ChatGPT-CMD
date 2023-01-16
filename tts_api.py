import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.1)

voices = engine.getProperty('voices')

for voice in voices:
    if 'Microsoft Zira Desktop - English (United States)' in voice.name:
        engine.setProperty('voice', voice.id)
        print("Voz actual: ", voice.name)
        break

def lain_say(text_to_speak="Hola"):
    engine.say(text_to_speak)
    engine.runAndWait()
