import os
from time import sleep
from random import randrange
import sqlite3


def main():

    #HACER QUE SE CREE EL ARCHIVO CUANDO PASE UNAS HORAS

    x_hours = randrange(1,4)
    sleep(x_hours * 60 * 60)

    #Ruta del archivo donde se creará
    # desktop_path = "C:\\Users\\alexc\\Downloads\\"

    user_path = "C:\\Users\\alexc"
    desktop_path = user_path + "\\Donwloads\\"

    # Crear archivo
    # a = open(desktop_path + "Para Ti.txt", "w")
    # #Escribir en el archivo
    # a.write("SOY TU MAYOR MIEDO PERRO DE MIERDA")
    # a.close()

    #HACERLO DE UNA MANERA MÁS CHULA
    with open( desktop_path + "XXX___s.txt", "w") as hackerFile:
        hackerFile.write("H9LA SOY EL HACKER DE TIIII")


    db_history= ""

    conect= sqlite3.connect(db_history)
    #Obtener nombre del user
    # print(os.getlogin())
if __name__ == '__main__':
    main()