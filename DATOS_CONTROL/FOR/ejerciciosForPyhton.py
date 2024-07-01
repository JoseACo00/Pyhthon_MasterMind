#EJERCICIOS PARA COMPRENDER MEJOR EL FOR EN PYTHON
import string
#1 SACAR DE UNA FRASE : LOS ESPACIOS, PUNTOS, COMAS

#espacio = 0
#puntos = 0
#comas = 0
#textoUser= input("Dime un texto: "
                # "\nTexto: ")

#for i in textoUser:

#   if i == " ":
#       espacio += 1
 #   elif i == ",":
#       comas += 1
 #   elif i == ".":
#       puntos += 1

#print("RESULTADO"
#     "\nCOMAS {}:".format(comas),
#   "\nPUNTOS {}:".format(puntos),
#     "\nESPACIOS {}:".format(espacio))


#2 CONTAR LAS MAYUSCULAS QUE TENGA UN TEXTO INTRODUCIDO POR EL USUARIO

n_Mayusculas = 0

#for i in textoUser:
 #   if i in string.ascii_uppercase:
  #      n_Mayusculas += 1

#print("HAY UN TOTAL DE LETRAS MAYUSCULAS EN EL TEXTO DE : {}".format(n_Mayusculas))


#3 TABLA DE MULTIPLICA QUE QUIERAS

numero = int(input("Dime que numero tabla quieres saber:" "\n NUMERO: "))
numero2 =  int(input("Dime hasta que n quieres que multiplice : "))
#for n in range(numero2):

 #   multi = numero * n
#    print(" {} x {} = {}".format(numero, n, multi))



# SOLO DEVOLVER LOS MULTIPLOS DE 2 DE UN NUMERO DESEADO EJEMPLO DE 12 SOLO QUIERE EL 2 EL 4 EL 9 ETC

for i in range(numero2):
    if i % 2 == 0:
        multi = numero * i
        print(" {} x {} = {}".format(numero, i, multi))
