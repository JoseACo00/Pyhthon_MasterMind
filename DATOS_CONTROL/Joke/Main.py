import os

def main():
    #Ruta del archivo donde se creará
    desktop_path = "C:\\Users\\alexc\\Downloads\\"


    # Crear archivo
    a = open(desktop_path + "Para Ti.txt", "w")

    #Escribir en el archivo
    a.write("SOY TU MAYOR MIEDO PERRO DE MIERDA")
    a.close()

    #Obtener nombre del user
    # print(os.getlogin())



if __name__ == '__main__':
    main()