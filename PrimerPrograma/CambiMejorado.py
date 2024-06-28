#VAMOS A REALIZAR UNA MEJORA EN LA CONVERSIONES DE LA MONEDA DE EURO, LIBRA, DOLAR


dolar_euro = 0.93
libra_euro = 1.19

opcion = input("DIME QUE CONVERSIÓN QUIERES REALIZAR"
               +"\n-1 LIBRA A EURO"
               +"\n-2 DOLAR A EURO"
               +"\n-3 EURO A LIBRA"
               +"\n-4 EURO A DOLAR"
               +"\n-OPCION: ")

if opcion == "1":
    valor_Libra = float(input("Dime cuantas libras quieres convertir"
                              +"\nLIBRAS: "))
    operacion1 = valor_Libra * libra_euro
    print("EL RESULTADO DE CONVERTIR {} LIBRAS A EUROS ES DE: {} €".format(valor_Libra, operacion1))
elif opcion == "2":
    valor_Dolar = float(input("Dime cuantos dolares quieres convertir"
                              +"\nDOLARES: "))
    operacion2 = valor_Dolar * dolar_euro
    print("EL RESULTADO DE CONVERTIR {}$ A EUROS ES DE: {} €".format(valor_Dolar,operacion2))

elif opcion == "3":
    valor_Euro = float(input("Dime cuantos euros quieres convertir a libras"
                             +"\nEUROS: "))
    operacion3 = valor_Euro * libra_euro
    print("EL RESULTADO DE CONVERTIR {} € A LIBRAS ES DE {} LIBRAS".format(valor_Euro,operacion3))

elif opcion == "4":
    valor_Euro = float(input("Dime cuantos euros quieres convertir a libra "
                             + "\nEUROS: "))
    operacion4 = valor_Euro * dolar_euro
    print("EL RESUTLADO DE CAMBIAR {} € A DOLARES ES DE {} $".format(valor_Euro,operacion4))
else:
    print("OPCION INVALIDA SOLO SE PUEDE 1 A 4")

## NO ES BUNEO TENER QUE REPETIR TANTO CODIGO PUEDES DEJAR LOS TEXTOS EN VARIABLES Y SOLO CAMBIARLO A TÚ REQUIRIMIENTO