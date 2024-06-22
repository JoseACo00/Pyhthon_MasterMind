#1 CONVERTIR DE GRADOS FARENGHAIS A CELCIUS

Farenghais= float;

print("ACTIVIDAD 1 \n ____________________________________")
print("VAMOS A CALCULAR LOS GRADOS DE FARENHAIT A CELCIUS")
faulthandler=  int(input("Dime los grados FARENHAIT que hace ahora :"))

#CALCULAR LOS CELCIUS
Celcius= (faulthandler - 32) * 5/9
print("Ahora hace una temperatura de Celcius "+ str(Celcius))

# CONVERTIR DE LIBRAS A EUROS
libras= float;
cambioEuros= float;
print("\nActividad 2 \n ___________________________________")
print ("VAMOS A CONVERTIR LAS LIBRAS DE UN CLIENTE A EUROS")
libras = float(input("Dime los cuantas libras quire cambiar el cliente: "))
cambioEuros = float(input("DIME A CUANTO ESTA EL CAMBIO AHORA "))
#CALCULAR LA CONVERTSION
resultado = libras * cambioEuros
print("El cambio de divisa de {}".format(libras),"libras a euros es: {}".format(resultado), "€")