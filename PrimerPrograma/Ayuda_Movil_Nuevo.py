#PROGRMAA PARA SABER QUE MOVIL TE CONVIENE MÁS POR UN TEST RÁPIDO HABRÁ 5 OPCIONES


dinero = "TIENES DINERO??"
camara = ""
opcion1 = "IPHONE ULTRA PRO MAX"
opcion2 = "IPHONE 2 MANO"
opcion3 = "ANDROID CHINO 100"
opcion4 = "GOOGLE PIXEL SUPER CAMERA"
opcion5 = "ANDROID CALIDAD-PRECIO"


sistema_Operativo = input("QUE SISTEMA OPERATIVO QUIERS android o ios ")
if sistema_Operativo != "ios":

    pregunta = input(dinero)
    if pregunta != "si":
        print("NO TIENES DINERO " +
              "\nTÚ MEJOR OPCIONE ES: " + opcion3)


    print("TIENES DINERO FELICIDADES !!! ")
    camera = input("TE IMPORTA LA CÁMARA EN TÚ DISPOSITIVO???? ")
    if camara != "si":
        print("NO TE IMPORTA LA CÁMARA POR ELLO LA MEJOR OPICON"+opcion5)
    elif camera == "si":
        print("TU MEJOR OPCIONES ES UN: " + opcion4)

elif sistema_Operativo == "ios":
    pregunta = input(dinero)

    if pregunta != "no":
        print("TIENES DINERO FELICIDEADES !!!"
              +"\nLA MEJOR OPCION ES" +opcion1)

    elif pregunta == "no":
        print("MI RECOMENDACION ES : "+opcion2)


else:
    print("DEBES ESCOGER UNA OPCION VALIDA android / ios")