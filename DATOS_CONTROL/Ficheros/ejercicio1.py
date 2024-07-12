lista_productos = ["pan", "arroz", "leche", "carne", "café"]
SALIDA = "salir"
ARCHIVO_LISTA = "archivoProductos.txt"

# #1# Ejercicio 1: Externalizar guardado
# # Mueve el código de guardar el archivo a una función externa

def guardarArchivo(lista_compra):
    # a = open(nombre_archivo+".txt", "w")
    # a.write(("----Productos de la compra----\n" + "\n".join(lista_compra) + "\n------------------------------"))
    # a.close()
    # nombre_archivo = input("nombre")
    #OTRA MANERA DE HACERLO
    with open(ARCHIVO_LISTA, "w") as archivo:
        archivo.write("----Productos de la compra----\n" + "\n".join(lista_compra))



def pregunta_usuario():
    producto_elegido= input("Ingrese el producto para la lista de la compra  (PARA SALIR: ESCRIBE {}): ".format(SALIDA) +
                 "\nProducto: ")

    return producto_elegido


# Ejercicio 2: Lista de productos fija
# De ahora en adelante el usuario solo podrá introducir los productos que estén en una lista especifica.
# Por ejemplo si nuestra lista tiene "Pan", "Pollo" y "Pipas", el usuario solo podrá meter en la lista de la compra uno de esos 3 items.
# Lo haremos comprobando que el texto introducido por el usuario está en la lista de productos preestablecidos.
# Si no lo está le daremos un mensaje avisándole que ese producto no está disponible para meter en la lista.

def completed_list(lista_compra):
    input_usuario = pregunta_usuario()

    while input_usuario.lower() != SALIDA:
        #LOWER EN INPUT DE USER POR SI ESCRIBRE LECHE LO PUEDA AGREGAR
        #LOWER EN LISTA PARA QUE LA LISTA SEA EN MINISCULAS Y NO LO QUE METE EL USER EJ : LecHE, se cambiaría  Leche y ya.

        if input_usuario.lower() not in [a.lower() for a in lista_productos]:
            print("El producto {} no está en la lista de productos, sorry".format(input_usuario))
            print(lista_productos)

        elif input_usuario.lower() in [a.lower() for a in lista_compra]:
            print("El producto ya está en tú lista")

        else:
            lista_compra.append(input_usuario)
            print("----Productos de la compra----\n" + "\n".join(lista_compra) + "\n------------------------------")

        input_usuario = pregunta_usuario()


# Ejercicio 3: Mostrar la lista
# Implementa el comando "LISTA" para ver los items disponibles que se pueden añadir a la lista, así el usuario sabe que
# puede meter en su
#lista de la compra y que no.
def producto_en_la_tienda():
    print("PRODUCTOS DE LA TIENDA\n"
         + "\n".join(lista_productos) + "\n------------------------------")

def menu():
    print("BIENVENIDO AL SUPER JOSECET "
          "\n1:Agregar prouducto"
          "\n2:Ver productos de la tienda"
          "\n3:Salir"
          "\n4:Modificar Archivo")
def main():
    lista_compra = []
    while True:
        menu()
        accion = input("\nAccion: ")

        if accion == "1":
            completed_list(lista_compra)
        elif accion == "2":
            producto_en_la_tienda()
        elif accion == "3":
            guardarArchivo(lista_compra)
            break
        elif accion == "4":
            with open(ARCHIVO_LISTA, "r") as archivo:
                lista_compra = archivo.read().split("\n")
        else:
            print("No es una opcion válida")


if __name__ == '__main__':
    main()
