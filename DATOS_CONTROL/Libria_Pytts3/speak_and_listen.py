import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty('rate', 200)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear_me():

    with sr.Microphone() as source:
        print("Escuchando.....")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es-Es")
            print("He entendio: {}".format(text))
            return text
        except sr.UnknownValueError:
            return


#SI NO QUEREMOS QUE SE EJECUTE PRUEBAS COMO ESTA CUANOD IMPORTAMOS ESTE ARCHIVO AL PRINCIPAL SE PONE EL IF __NAME ...
# SI SE EJECUTA DESDE AQUI SI LO HACE PERO SI LO HACE DESDE OTRO ARCHIVO AUNQUE SE IMPORTE NO SE EJECUTA LO DE DENTRO
if __name__ == "__main__":
    speak("Probando si funciona")
    hear_me()