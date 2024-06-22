#a = 2
""" print(a)
a= a * 8
print(a)

a = "hola"
print(a)"""

#ESCRIBIR EN LA CONSOLA
"""nombre= input("?Cual es tú nombre?: ")
print("Tú nombre es: -> " + nombre

IMPUT SIEMPRE DE VUELVE UN STR SI QUIERES OTRO TIPO DE DATO LO DEBES CONCATENAR ANTES DEL INPUNT CON EL NONMBRE DE LA VARIABLE QUE DESEAS
EJ:
NUMER= INT(INPUT(DIME EL NUMERICO PERRO));
SERÁ INT
"""

#(max) Es para buscar el número más alto de un valor x de números
#min Da el valor  más pequeño de una entrada x de números
"""max(1, 2, 3, 4, 45, 232)
min(2,32,32,121,41321)"""

numerA= int(input("DIME EL 1 NÚMERO "))
numerB= int(input("DIME EL 2 NÚMERO "))
numerC= int(input("DIME EL 3 NÚMERO "))

print("Te voy a decir el número máximo de valor y el mínimo de\n"
      +"\nEl máximo es : "+ str(max(numerA,numerB,numerC))
      +"\nEl minimo es : "+ str(min(numerA,numerB,numerC)))


#SEGUNDA MANERA CON EL .FORMAT
print("__________________________________")
print("SEGUNDA MANERA DE VISUALIZAR\n")
print("El NÚMERO MAS DRANDE ENTRE {}, {} Y  {} ES: \n(MAYOR): {} \n(Minimo) {}".format( numerA, numerB, numerC, max(numerA,numerB,numerC), min(numerA,numerB,numerC)))

