#JUEGO PARA PODER HACER UN LABERINOT
from random import randint, random
import os

import readchar

POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

NUM_MAX_OBJECTS_MAPS = 11
tail_Lenght = 0
tail = []
my_position = [3,1]

#HACER QUE SE GENEERE 10 DE ESTOS A LEATORIAMENTE

map_Objects= []
# for a in range(10): ES MEJOR REALIZAR UN WHILE POR QUE CON EL FOR PODEMOS REPITIR ALGO SEGUN NATE
#     position_randomX = randint(2, 19)
#     position_randomY = randint(2, 14)
#     map_Objects.append([position_randomX, position_randomY ])

while len(map_Objects) < NUM_MAX_OBJECTS_MAPS:

    new_Position = [randint(0,MAP_WIDTH), randint(0,MAP_HEIGHT)]

    if new_Position not in map_Objects and new_Position != my_position: #ES DISTINTO DE MI LISTA Y DIFERENTE EN MI POSICION INICIAL
        map_Objects.append(new_Position)
#DIBUJAR EL MAPA
# print("+" + "-" * MAP_WIDTH * 3 + "+")
#
# for cordinate_Y in range(MAP_HEIGHT):s
#     print("|", end="")
#     for coordinate_x in range(MAP_WIDTH):
#         if my_position[POS_X] == coordinate_x and my_position[POS_Y] == cordinate_Y:
#             print(" @ ", end="")
#         else:
#             print("   ", end="")
#     print("|")
# print("+" + "-" * MAP_WIDTH * 3 + "+")
#
# #MOVE THE USER
#
# #direction = input("Donde te quieres moder? [WASD]"
#                   # "/nDIRRECION: ")
# direction = readchar.readchar()
#
# print(direction)
#
# if direction == "w":
#     my_position[POS_Y] -= 1
# elif direction == "s":
#     my_position[POS_Y] += 1
# elif direction == "a":
#     my_position[POS_X] -= 1
# elif direction == "d":
#     my_position[POS_X] += 1
#
# #DIBUJAR EL MAPA
# print("+" + "-" * MAP_WIDTH * 3 + "+")
#
# for cordinate_Y in range(MAP_HEIGHT):
#     print("|", end="")
#     for coordinate_x in range(MAP_WIDTH):
#         if my_position[POS_X] == coordinate_x and my_position[POS_Y] == cordinate_Y:
#             print(" @ ", end="")
#         else:
#             print("   ", end="")
#     print("|")
# print("+" + "-" * MAP_WIDTH * 3 + "+")


#PARA HACER QUE NO SE REPITA TANTO LAS COSAS VAMOS A REALIZAR UN WHILE TRUE PARA QUE SEIMPRE REPITA LAS COSAS

while True:
    # DIBUJAR EL MAPA
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_Y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw =" "

            #DIBUJAR LOS OBJETOS PARA RECOGER
            for map_Object in map_Objects:
                if map_Object[POS_X] == coordinate_x and map_Object[POS_Y] == cordinate_Y:
                    char_to_draw = "º"

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == cordinate_Y:
                    char_to_draw = "@"
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == cordinate_Y:
                char_to_draw = "@"
                for map_Object in map_Objects:
                    if my_position[POS_X] == map_Object[POS_X] and my_position[POS_Y] == map_Object[POS_Y]:
                        map_Objects.remove(map_Object)
                        tail_Lenght += 1 #CRECE 1 MI COLA CUANDO COMEMEMOS UN CASILLA

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    # print("TAMAÑO DE COLA : {}".format(tail_Lenght))
    print("LA COLA : {}".format(tail))


    # MOVE THE USER

    # direction = input("Donde te quieres moder? [WASD]"
    # "/nDIRRECION: ")
    direction = readchar.readchar()

    print(direction)

    if direction == "w":
        tail.insert(0, my_position.copy()) #INSERTA EN LA LISTA EN LA 1 POSCION LA 0 LA POSICION ANTES DE MOVERTE SI ESTABAS EN LA 2.2 SE METE EN LISTA[ [2,2] ]
        tail = tail[:tail_Lenght]
        my_position[POS_Y] -= 1
        if my_position[POS_Y] < 0:
            my_position[POS_Y] = MAP_HEIGHT -1
    elif direction == "s":
        tail.insert(0, my_position.copy())
        my_position[POS_Y] += 1
        tail = tail[:tail_Lenght]
        if my_position[POS_Y] >= MAP_HEIGHT:
            my_position[POS_Y] = 0
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_Lenght]
        my_position[POS_X] -= 1
        if my_position[POS_X] < 0:
            my_position[POS_X] = MAP_WIDTH -1
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_Lenght]
        my_position[POS_X] += 1
        if my_position[POS_X] >= MAP_WIDTH:
            my_position[POS_X]= 0
    elif direction == "t":
        break  #SALIMOS DEL BUCLE WHILE  ROMPE EL WHILE
    os.system("cls")
