#BOOL OPERACIONES

edad= int(input("Dime la edad que tienes: "))
t_Carnet = input("Dime el tipo de carnet que tienes ( E, P , F, N)"
                 "\nE = ESTUDIANTE"
                 +"\nP = PENSIONISTA"
                 +"\nF = FAMILIA NUMEROS"
                 +"\nN = NADA"
                 "\n : ")

if ( edad <= 35 and edad >= 25 and t_Carnet == "E" ) or edad <= 10 or  (edad >= 65 and t_Carnet =="P") or (t_Carnet == "F"):
    print("Tiene posibilidad de obtar al 25% de descuentos. Felicidades!!!!")
else:
    print("No tienes ningun descuento")