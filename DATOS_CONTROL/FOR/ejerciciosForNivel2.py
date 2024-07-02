# BUSCAR EL NUMERO MAS PEQUEÑO , MAS GRANDE
lista_numeros = []



#1 funcion
# def mayorNumero(lista):
#     max = lista[0]
#     for i in lista:
#         if i > max:
#             max = i
#
#     return max
#
# def menorNumero(lista):
#     min = lista[0]
#     for i in lista:
#         if i < min:
#             min = i
#     return min
# accion = None
# while accion != "S":
#     accion  = input("A AGREGAR NUMERO"
#           "\nS SALIR"
#           "\nAccion: ")
#     if accion == "A":
#         print("DIME QUE NUMERO QUIERES AGREGAR")
#         num = int(input("Numero: "))
#         lista_numeros.append(num)
#     elif accion == "S":
#         print("Salir de esto")
#
#
# print("LOS NUMEROS SON"
#       "\nPEQUEÑO: {}".format(menorNumero(lista_numeros)),
#       "\nMAYOR: {}".format(mayorNumero(lista_numeros)))

#OTRAS MANERAS DE HACERLO

#1
# numero_Introducido = int(input("INTROCE EL NUMERO EN LA LISTA: "))
# lista_numeros.append(numero_Introducido)
#
# while input("Deseas introducir  más numeros [S/N: " ) != "N":
#     numero_Introducido = int(input("INTROCE EL NUMERO EN LA LISTA:  "))
#     lista_numeros.append(numero_Introducido)
#
# print(lista_numeros)

#2 SEGUNDA MANERA

numeroIntroducidos = input("Introduzca los numeros separados por comas : ")
numeroLista = numeroIntroducidos.split(",") #
# numeroInt = []
# print(numeroLista) #LISTA DE STRING NO DE INT
#  #TRANSFORMAR ESE STRINGA  INT
# for numero in numeroLista:
#     numeroInt.append(int(numero)) #LO CONCATENAMOS
# print("LISTA DE NUMERO EN INT : ",numeroInt)
#2 UTILIZANDO LA LIST COMPREHESION

numeroUsuario = [int(numero) for numero in numeroLista] # Numero in numerolista una conversion con el int(numero)
print(numeroUsuario)

numeroPequenio = numeroUsuario[0]
numeroMayor = numeroUsuario[0]

for numero in numeroUsuario[1:]:
    if numero < numeroPequenio:
        numeroPequenio = numero
    if  numeroMayor < numero:
        numeroMayor = numero

print("LOS NUMEROS SON"
       "\nPEQUEÑO: {}"
       "\nMAYOR: {}".format( numeroPequenio,numeroMayor))