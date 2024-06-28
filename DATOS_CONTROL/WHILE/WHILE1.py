#VAMOS A VER EL USO DEL WHILE

#1
#HACER QUE ELIJA UNA RESPUTAS QUE NOS PAREZCA BIEN O DESEAMOS
# respuesta = None
# while respuesta != "A" and respuesta != "B" and respuesta != "C" :
#     respuesta = input("DIME A ,B,  o C"
#                       "\nOPCION: ")
#
# if respuesta == "A":
#     print("TU RESPUESTA FUE LA A")
#
# elif respuesta == "B":
#     print("TU RESPUESTA FUE LA B")
#
# elif respuesta == "C":
#     print("Tu respuesta fue la c ")
#
# else:
#     print("Tu RESPUESTAS NO ES VALIDA"
#           "\n INTENTALO DE NUEVO...")


#2
#PODEMOS HACER QUE SE TERMINE HASTA QUE LLEGE A UN NUMERO O SE MENOR A UNO
numero = 12

while numero > 1:
    #numero += 1 AUMENTA
    #numero -= 1 DECRECE UNO
    numero -= 1
    print("MI NUMERO {} ES MAYOR QUE UNO".format(numero))
