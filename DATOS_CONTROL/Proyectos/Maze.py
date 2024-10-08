#JUEGO PARA PODER HACER UN LABERINOT

#IMPORTS

from random import randint, random
import os
import readchar

#END IMPORTS

#VARIABLES TO GAMES
POS_X = 0
POS_Y = 1

# MAP_WIDTH = 20 SE VA CALCULAR AHORA DEPENDIENTO DE COMO SE A EL OBSTACLE MAPPS
# MAP_HEIGHT = 15

NUM_MAX_OBJECTS_MAPS = 11

#DRAW THE MAP  OBSTACLE ANDA AFTER IT WILL BE A LIST, BROKEN THIS STRING

obstacle_Definition = """\
###############################
#                             #
# ############  #### #    ### #
#         ###        ###    # #
#   ##### ### ##     ###    # #
#       # ### #    #####    # #
#     # # ### #     ######### #
#  ##   # ### # #     # ##### #
#   #   # ### # ####    ##### #
### #   # ### # ####    ##### #
### #   # ##            ##### #
###     #  ## #     # # ##### #
### ### #  ## #         ##### #
#######   ### # # # #         #
###############################\
"""

my_position = [0, 1]

tail_Lenght = 0
tail = []
end_Game = False #VARIABLE PARA TERMINAR EL JUEGO / EN SWICH SERA FALSE HASTA QUE ESTE UN TRUE QUE SERA FIN DE JEUGO
map_Objects = []

#END TO VARAIBLES TO THE GAME


#CREATE OBSTACLE MAPS (SE PARAR POR CADA ENTER UNA LINEA DISTINTA)
# obstacle_Definition = obstacle_Definition.split("\n")
# print(obstacle_Definition)
#VAMOS A REALIZAR UNA LIST COMPREGENTION
obstacle_Definition = [list(row) for row in obstacle_Definition.split("\n")]  #I CREATE A LIST OF STRING

MAP_WIDTH = len(obstacle_Definition[0])
MAP_HEIGHT = len(obstacle_Definition)
#print(obstacle_Definition)

# Función para limpiar la pantalla
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#HACER QUE SE GENEERE 10 DE ESTOS A LEATORIAMENTE
# while len(map_Objects) < NUM_MAX_OBJECTS_MAPS:
#     new_Position = [randint(0,MAP_WIDTH), randint(0,MAP_HEIGHT)]
#     if new_Position not in map_Objects and new_Position != my_position: #ES DISTINTO DE MI LISTA Y DIFERENTE EN MI POSICION INICIAL
#         map_Objects.append(new_Position)


# MANERA DISTINTA CON LA VARIABLE OBJECT IN CELL
#MAIN LOOP
while not end_Game:
    clear_screen()
    # HACER QUE SE GENEERE 10 DE ESTOS A LEATORIAMENTE
    while len(map_Objects) < NUM_MAX_OBJECTS_MAPS:
        new_Position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]

        if new_Position not in map_Objects and new_Position != my_position and \
                obstacle_Definition[new_Position[POS_Y]][
                    new_Position[POS_X]] != "#":  # ES DISTINTO DE MI LISTA Y DIFERENTE EN MI POSICION INICIAL
            map_Objects.append(new_Position)

    # DIBUJAR EL MAPA
    print("+" + "-" * MAP_WIDTH * 2 + "+")
    for coordinate_Y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tell_in_cell_ = None

            # DIBUJAR LOS OBJETOS PARA RECOGER
            for map_Object in map_Objects:
                if map_Object[POS_X] == coordinate_x and map_Object[POS_Y] == coordinate_Y:
                    char_to_draw = " º"
                    object_in_cell = map_Object

            # FOR DRAWING THE TAIL OF SNAKE
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_Y:
                    char_to_draw = " @"
                    tell_in_cell_ = tail_piece

            # DRAWING THE POSITION OF USER/SNAKE
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_Y:
                char_to_draw = " @"

                if object_in_cell:
                    map_Objects.remove(object_in_cell)
                    tail_Lenght += 1
                if tell_in_cell_:
                    char_to_draw = " "
                    end_Game = True
                    break

            # FOR A WHAT A OBSTACLE WITH IN POSITON
            if obstacle_Definition[coordinate_Y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")
    # print("TAMAÑO DE COLA : {}".format(tail_Lenght))
    # print("LA COLA : {}".format(tail))

    # MOVE THE USER

    # direction = input("Donde te quieres moder? [WASD]"
    # "/nDIRRECION: ")
    direction = readchar.readchar()

    new_position = None
    # print(direction)

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "t":
        end_Game = True

    if new_position:
        if obstacle_Definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_Lenght]
            my_position = new_position


# Mostrar mensaje de fin del juego
clear_screen()
end_message = " END GAME "
start_x = (MAP_WIDTH * 3 - len(end_message)) // 2

print("+" + "-" * MAP_WIDTH * 3 + "+")
for y in range(MAP_HEIGHT):
    if y == MAP_HEIGHT // 2:
        print("|" + " " * start_x + end_message + " " * (MAP_WIDTH * 3 - start_x - len(end_message)) + "|")
    else:
        print("|" + " " * (MAP_WIDTH * 3) + "|")
print("+" + "-" * MAP_WIDTH * 3 + "+")









#COMENTARIOS QUE SON CODIGO QUE HICE Y ESTÁN BIEN PERO SON OTROS PUNTOS DE VISTA LO DE ARRIBA
# for a in range(10): ES MEJOR REALIZAR UN WHILE POR QUE CON EL FOR PODEMOS REPITIR ALGO SEGUN NATE
#     position_randomX = randint(2, 19)
#     position_randomY = randint(2, 14)
#     map_Objects.append([position_randomX, position_randomY ])

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

# while True:
#     # DIBUJAR EL MAPA
#     print("+" + "-" * MAP_WIDTH * 3 + "+")
#
#     for cordinate_Y in range(MAP_HEIGHT):
#         print("|", end="")
#         for coordinate_x in range(MAP_WIDTH):
#
#             char_to_draw =" "
#             tell_in_cell_nos = None
#             #DIBUJAR LOS OBJETOS PARA RECOGER
#             for map_Object in map_Objects:
#                 if map_Object[POS_X] == coordinate_x and map_Object[POS_Y] == cordinate_Y:
#                     char_to_draw = "º"
#             #FOR DRAWING THE TAIL OF SNAKE
#             for tail_piece in tail:
#                 if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == cordinate_Y:
#                     char_to_draw = "@"
#             #DRAWING THE POSITION OF USER/SNAKE
#             if my_position[POS_X] == coordinate_x and my_position[POS_Y] == cordinate_Y:
#                 char_to_draw = "@"
#                 for map_Object in map_Objects:
#                     if my_position[POS_X] == map_Object[POS_X] and my_position[POS_Y] == map_Object[POS_Y]:
#                         map_Objects.remove(map_Object)
#                         tail_Lenght += 1 #CRECE 1 MI COLA CUANDO COMEMEMOS UN CASILLA