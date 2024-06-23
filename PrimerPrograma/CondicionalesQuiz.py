#VAMOS A REALIZAR UN QUIZ DE FUTBOL SOBRE EL REAL MADRID

puntuacion=0

print("VAMOS A REALIZAR UN QUIZ SOBRE EL REAL MADRID")

option=input("\n1 PREGUNTA"
      +"\nCUANTAS CHAMPIONS TIENE EL MADRID"
      +"\n A 15"
      +"\n B 45"
      +"\n C 14"
      +"\n D 11"
      + "\n RESPUESTA: ")

#ELIF ES COMO UN (PERO) LA OPCION BUENA ES LA A PERO SINO LA B O SINO LA C O LA D
if option== "A":
    puntuacion += 10
elif option== "B":
    puntuacion += 0
elif option == "C":
    puntuacion += 5
elif option == "D":
    puntuacion += 2
else:
    print("NECESITA PONER UNA OPCIÓN VÁLIDA")
    exit()


option=input("\n2 PREGUNTA"
      +"\nCUANDO SE FUNDO EL REAL MADRID"
      +"\n A 1923"
      +"\n B 1901"
      +"\n C 2002"
      +"\n D 1902"
      + "\n RESPUESTA: ")
if option== "A":
    puntuacion += 2
elif option== "B":
    puntuacion += 5
elif option == "C":
    puntuacion += 0
elif option == "D":
    puntuacion += 10
else:
    print("NECESITA PONER UNA OPCIÓN VÁLIDA")



option = input("\n3 PREGUNTA"
      +"\nCUANTAS LIGAS TIENE EL REAL MADRID"
      +"\n A 26"
      +"\n B 36"
      +"\n C 35"
      +"\n D 31"
      + "\n RESPUESTA: ")

if option== "A":
    puntuacion += 0
elif option== "B":
    puntuacion += 10
elif option == "C":
    puntuacion += 5
elif option == "D":
    puntuacion += 2
else:
    print("NECESITA PONER UNA OPCIÓN VÁLIDA")

option = input("\n4 PREGUNTA"
      +"\nCUANTAS COPA DEL REY TIENE"
      +"\n A 20"
      +"\n B 41"
      +"\n C 21"
      +"\n D 17"
      + "\n RESPUESTA: ")

if option == "A":
    puntuacion += 10
elif option == "B":
    puntuacion += 0
elif option == "C":
    puntuacion += 5
elif option == "D":
    puntuacion += 2
else:
    print("NECESITA PONER UNA OPCIÓN VÁLIDA")


if puntuacion >=35:
    print("ERES UN GRAN FAN DEL REAL MADRID"+
          "\nPUNTOS {}".format(puntuacion))
elif puntuacion >=25:
    print("ERES UN BUEN FAN DEL REAL MADRID"
          +
          "\nPUNTOS {}".format(puntuacion))
elif puntuacion >=15:
    print("ERES UN MEDIO FAN DEL REAL MADRID"
          +
          "\nPUNTOS {}".format(puntuacion))
elif puntuacion >=10:
    print("NO SABES NADA DEL REAL CABRON"+
          "\nPUNTOS: {}".format(puntuacion))
