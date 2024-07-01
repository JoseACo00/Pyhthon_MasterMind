# BUSCAR EL NUMERO MAS PEQUEÑO , MAS GRANDE
lista_numeros = []



#1 funcion
def mayorNumero(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i

    return max

def menorNumero(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min
accion = None
while accion != "S":
    accion  = input("A AGREGAR NUMERO"
          "\nS SALIR"
          "\nAccion: ")
    if accion == "A":
        print("DIME QUE NUMERO QUIERES AGREGAR")
        num = int(input("Numero: "))
        lista_numeros.append(num)
    elif accion == "S":
        print("Salir de esto")


print("LOS NUMEROS SON"
      "\nPEQUEÑO: {}".format(menorNumero(lista_numeros)),
      "\nMAYOR: {}".format(mayorNumero(lista_numeros)))

#OTRAS MANERAS DE HACERLO

#1
#2
#2