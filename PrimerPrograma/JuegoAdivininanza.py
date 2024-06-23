#JUEGO PARA ADIVINAR UN NÚMERO

#LAS FUNCIONES ESPECIALES SEBE IMPORTAR
import random


nGanador = random.randint(1,10)

intento = int(input("Dime el número que crees que estoy pensando ahora  de 1 a 10:  "))

if intento <0 or intento > 10:
    print("EL RANGO ES DE 1 A 10 RECUERDA")

if intento != nGanador:
    print("Losiento el número {}".format(intento), " no es el correcto")

if intento == nGanador:
    print("Correcto el número que estaba pensando es el {}".format(nGanador))