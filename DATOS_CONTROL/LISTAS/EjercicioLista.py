import os
#EJERCICIO PARA SIMULAR UN LISTA DE LA COMPRA DONDE LO QUE VAYAMOS A PONER SE INTROUDUCE EN UN ARRAY/LISTA

lista_Compra = []
accion = None

print("----VAMOS REALIZAR LA LISTA DE LA COMPRA DIME QUE QUIERES COMPRAR--------")

while accion != "S":
    print("\n--ACCIONES--"
          "\n A --> Agregar productoa  para la compra"
          "\n Q --> Eliminar ultimo elemento de la lista de la compra"
          "\n W --> VER LISTA DE LA COMPRA"
          "\n S----> SALIR")

    accion = input("RESPUESTA: ")
    if accion == "A":
        print("\nDIME QUE PRODUCTO QUIERES AGREGAR")
        producto= input("NOMBRE: ")
        print("SEGURO QUE QUIERES AGREGAR : {} ?".format(producto))
        respuesta = input("RESPUESTA: S(SI) / N(NO):"
                              "\nACCION: ")
        if respuesta == "S":
            if producto in lista_Compra:
                print("EL PRODUCTO YA ESTA EN LA LISTA")
                os.system('cls')
            else:
                print("SE AGREGÓ EL PRODUCTO {}".format(producto))
                lista_Compra.append(producto)
            os.system('cls')
        else:
            print("NO SE AGREGO NADA")
        os.system('cls')
    elif accion == "Q":
        lista_Compra.pop()
        print("LISTA DE LA COMPRA ACTUALIZADA: ",(lista_Compra))

    elif accion == "W":
        print("LISTA DE LA COMPRA ACTUALES: \n",lista_Compra)

    elif accion == "S":
        break

if len(lista_Compra) != 0:

    print("---LA LISTA DE LA COMPRA FINAL---------")
    print("--",lista_Compra)
    print("-----------------------------------------")
    exit()

print("NO HAS COMPRANADA TODAVIA")

