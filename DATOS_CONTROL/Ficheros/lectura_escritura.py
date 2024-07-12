

SALIDA = "salir"

def pregunta_usuario():
    return input("Ingrese el producto para la lista de la compra  (PARA SALIR: ESCRIBE {}): ".format(SALIDA)+
                 "\nProducto: ")
def main():
    lista_compra = []

    input_usuario = pregunta_usuario()

    while input_usuario != SALIDA:

        if input_usuario in lista_compra:
            print("El producto ya esta en la lista")
            print(lista_compra)

        lista_compra.append(input_usuario)
        print("----Productos de la compra----\n" + "\n".join(lista_compra) + "\n------------------------------")
        input_usuario = pregunta_usuario()

        #CREAR TXT
    a = open("ListaCormpra.txt", "w")
    a.write(("----Productos de la compra----\n" + "\n".join(lista_compra) + "\n------------------------------"))
    a.close()




if __name__ == '__main__':
    main()