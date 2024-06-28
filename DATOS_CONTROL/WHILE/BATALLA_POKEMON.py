from random import randint

#BATALLA ENTRE PIKACHU (CPU) Y SQUARTLE (NOSOTROS)

#PIKACHU
  # VIDA: 80
  # MOVIMIENTOS:
  #   BOLA VOLTIO : 10
  #   ONDA TRUENO : 11

#SQUARTLE
    # VIDA: 90
    # MOVIMIENTOS:
        # PLACAJE : 10
        # PISTOLA AGUA: 12
        # BURBUJA: 9


vidaInicial_Pikachu = 80
vidaInicial_Squartle = 90

vidaActual_Pikachu = vidaInicial_Pikachu
vidaActual_Squartle = vidaInicial_Squartle

while vidaActual_Pikachu >= 0 and vidaActual_Squartle >= 0:
    print("---COMBATE POKEMON-----")
     #SE REALIZA LA ACCION DEL WHILE HASTA QUE NO PIERDA UNO

    print("\n----TURNO PIKACHU----")
    print("\nLA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        vidaActual_Squartle -= 10
        # BOLA VOLTIO : -10
        print("\nATACA PIKACHU CON : BOLA VOLTIO (-10)")

    else:
        print("ATACA PICACHU CON ONDA TRUENO (-11) ")
        vidaActual_Squartle -= 11

    input("\nPULSA ENTER PARA CONTINUAR...")

    #TURNO SQUARLTEl
    print("\n---TURNO DE SQUARTLE---")
    ataque_Squartle = None
    print("LA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
    while ataque_Squartle != "1" and ataque_Squartle != "2" and ataque_Squartle != "3":
        print("ESCOGE EL ATAQUE DE SQUARTLE")
        ataque_Squartle = input("\n(A)PLACAJE"
                                "\n(B)PISTOLA AGUA"
                                "\n(C)BURBUJA"
                                "\nACCION: ")

        if ataque_Squartle == "1":
            print("ATACA SQUARTLE CON: PLACAJE (-10)")
            vidaActual_Pikachu -= 10

        elif ataque_Squartle == "2":
            print("ATACA SQUARTLE CON: PISTOLA AGUA (-12)")
            vidaActual_Pikachu -= 12

        elif ataque_Squartle == "3":
            print("ATACA SQUARTLE CON: BURBUJA (-9)")
            vidaActual_Pikachu -= 9

        input("\nPULSA ENTER PARA CONTINUAR...")



if vidaActual_Pikachu > vidaActual_Squartle:
    print("\n----GANO PIKACHU--")
    print("LA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
else:
    print("\n----GANO SQUARTLE----")
    print("LA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
    
    
#HACER VIDA