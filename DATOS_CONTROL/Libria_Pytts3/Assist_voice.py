import re
import pyttsx3
import speech_recognition as sr
from time import sleep

#IMPORTAR FUNCIONES DE OTROS ARCHIVOS
from speak_and_listen import  hear_me

#pip install setuptools
#pip install pyttsx3 SpeechRecognition pyaudio

#pip install SpeechRecognition
#pip install pyaudio

#1 CREAR VARAIABLE PARA INICIALIZAR EL MOTOR DE HABLA
engine = pyttsx3.init()

#2 PONER LOS SETTINGS
engine.setProperty("voice", "spanish")

#NECESRIO INSTALAR PY AUDIO
engine.say("QUIEN VA A GANAR EL BALON DE ORO 2024")


#HOLA QUE HACE ES REPRODUCIR ESTE AUDIO
engine.runAndWait() #INSTALAR LA LIBREIA DE RECOGNITIONO PARA PODER INTERACTUAR POR VOZ

r = sr.Recognizer() #ELEMENTO PARA RECONOCER EL AUDIO
#


def initialize_engine():
    engine = pyttsx3.init()
    # engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    return engine

def winner_ball_of_dor(text):
    while True:
        engine.say("DIME YA QUIEN  ES EL JUSTO GANADOR DEL BALON DE ORO DESGRACIDADO")
        engine.runAndWait()  # INSTALAR LA LIBREIA DE RECOGNITIONO PARA PODER INTERACTUAR POR VOZ
        text = hear_me()

        if "Cristiano" in text or "cristiano" in text:
            engine.say(
                "SI, ESE ES EL QUE VA A GANAR SE LO MERECE TODO , MI BICHO, MI COMANDANTE, EL ASTRO LUSO, SI JODER PORFIN ACIERTAS MIERDOSO, ANDA EDU AGUIRRE ANDA COCINAR QUE SON LAS 2 QUIERES LECHE DEL BICHO")
            engine.runAndWait()
            break

        elif "Lamin" in text or "lamin" in text:
            engine.say(
                "SI GANA {} YAMAL, VA A GANAR LA COPA CUSCUS PREFIERO QUE EL , BALON DE ORO SEA  PARA MESSI PAPA".format(
                    text))
            engine.runAndWait()
        else:
            engine.say(
                "{} ESE CABRON NO JUEGA NI AL GUARZON PERO   ,  ESE SE LO MERECE MÁS QUE MONICIUS EL 7 DEL MADRID, ANDA VINI , ANDA PAIAA".format(text))

            engine.runAndWait()


def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombres es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name


def main():
    engine = initialize_engine()
    text = hear_me()
    winner_ball_of_dor(text)


if __name__ == '__main__':
    main()







#
# while True:
#     engine.say("DIME YA QUIEN  ES EL JUSTO GANADOR DEL BALON DE ORO DESGRACIDADO")
#     engine.runAndWait()# INSTALAR LA LIBREIA DE RECOGNITIONO PARA PODER INTERACTUAR POR VOZ
#     text = listen()
#
#     if "Cristiano" in text or "cristiano" in text:
#         engine.say("SI, ESE ES EL QUE VA A GANAR SE LO MERECE TODO , MI BICHO, MI COMANDANTE, EL ASTRO LUSO, SI JODER PORFIN ACIERTAS MIERDOSO, ANDA EDU AGUIRRE ANDA COCINAR QUE SON LAS 2 QUIERES LECHE DEL BICHO")
#         engine.runAndWait()
#         break
#
#     elif "Lamin" in text or "lamin" in text:
#         engine.say("SI GANA {} YAMAL, VA A GANAR LA COPA CUSCUS PREFIERO QUE EL , BALON DE ORO SEA  PARA MESSI PAPA".format(text))
#         engine.runAndWait()
#     else:
#         engine.say("{} ESE CABRON NO JUEGA NI AL GUARZON PERO   ,  ESE SE LO MERECE MÁS QUE MONICIUS EL 7 DEL MADRID, ANDA VINI , ANDA PASHAA" .format(text))
#         engine.runAndWait()


#SE CAMBIO POR LA FUNCION DE LISTEN AND HEARME
# def listen():
#     with sr.Microphone() as source:
#         print("Puedes hablar")
#         audio = r.listen(source)
#         text = r.recognize_google(audio, language="es-ES")
#         print("LO QUE HAS DICHO: "+"\n {}".format(text))
#         return text
