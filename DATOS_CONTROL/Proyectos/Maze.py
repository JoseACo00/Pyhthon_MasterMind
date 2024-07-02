#JUEGO PARA PODER HACER UN LABERINOT


POS_X = 0
POS_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3,1]




#DIBUJAR EL MAPA
print("+" + "-" * MAP_WIDTH * 3 + "+")

for cordinate_Y in range(MAP_HEIGHT):
    print("|", end="")
    for coordinate_x in range(MAP_WIDTH):
        if my_position[POS_X] == coordinate_x and my_position[POS_Y] == cordinate_Y:
            print(" @ ", end="")
        else:
            print("   ", end="")
    print("|")
print("+" + "-" * MAP_WIDTH * 3 + "+")