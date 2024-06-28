from random import randint
import os
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

#CONSTANTES EN MAYUSCULAS
TAMANIO_BARRA_PIKA = 20
TAMANIO_BARRA_SQUARTLE = 20


vidaInicial_Pikachu = 80
vidaInicial_Squartle = 90

vidaActual_Pikachu = vidaInicial_Pikachu
vidaActual_Squartle = vidaInicial_Squartle

while vidaActual_Pikachu >= 0 and vidaActual_Squartle >= 0:
    print("---COMBATE POKEMON-----")
     #SE REALIZA LA ACCION DEL WHILE HASTA QUE NO PIERDA UNO

    print("\n----TURNO PIKACHU----")

    barra_dePikachu = int(vidaActual_Pikachu * TAMANIO_BARRA_PIKA / vidaInicial_Pikachu)
    barra_deSquartle = int(vidaActual_Squartle * TAMANIO_BARRA_SQUARTLE / vidaInicial_Squartle)
    print("PIKACHU:  [{}{}] ({}/{})".format("*" * barra_dePikachu, " " * (TAMANIO_BARRA_PIKA - barra_dePikachu),
                                    vidaActual_Pikachu, vidaInicial_Pikachu))

    print("SQUARTLE:  [{}{}] ({}/{})".format("*" * barra_deSquartle, " " * (TAMANIO_BARRA_SQUARTLE - barra_deSquartle),
                                     vidaActual_Squartle, vidaInicial_Squartle))
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        vidaActual_Squartle -= 10
        # BOLA VOLTIO : -10
        print("\nATACA PIKACHU CON : BOLA VOLTIO (-10)")

    else:
        print("ATACA PICACHU CON ONDA TRUENO (-11) ")
        vidaActual_Squartle -= 11

    input("\nPULSA ENTER PARA CONTINUAR...")
    os.system('cls')


    #TURNO SQUARLTEl
    print("\n---TURNO DE SQUARTLE---")
    ataque_Squartle = None

    print("PIKACHU:  [{}{}] ({}/{})".format("*" * barra_dePikachu, ""*(TAMANIO_BARRA_PIKA - barra_dePikachu),
                                            vidaActual_Pikachu, vidaInicial_Pikachu))

    print("SQUARTLE:  [{}{}] ({}/{})".format("*" * barra_deSquartle, " " * (TAMANIO_BARRA_SQUARTLE - barra_deSquartle),
                                             vidaActual_Squartle, vidaInicial_Squartle))

    while ataque_Squartle != "1" and ataque_Squartle != "2" and ataque_Squartle != "3" and ataque_Squartle != "4":
        print("ESCOGE EL ATAQUE DE SQUARTLE")
        ataque_Squartle = input("\n(1)PLACAJE"
                                "\n(2)PISTOLA AGUA"
                                "\n(3)BURBUJA"
                                "\n(4)NADA"
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
        elif ataque_Squartle == "4":
            print("NO SE HIZO NADA")
            vidaActual_Pikachu -= 0
        input("\nPULSA ENTER PARA CONTINUAR...")
        os.system('cls')



if vidaActual_Pikachu > vidaActual_Squartle:
    vidaActual_Squartle =0
    print("\n----GANO PIKACHU--")
    print("LA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
else:
    print("\n----GANO SQUARTLE----")
    vidaActual_Pikachu = 0
    print("LA VIDA DE SQUARTLE ES: {} , PIKACHU VIDA: {}".format(vidaActual_Squartle, vidaActual_Pikachu))
    
    
#HACER VIDA