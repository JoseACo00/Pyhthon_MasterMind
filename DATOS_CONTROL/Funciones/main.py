#FUNCIONES
#SIRVEN PARA GUARDAR UNA SECUENCIA DE CODIGO BAJO EL NOMBRE PARA PODER EJECUTARLAS HACIENDO REFERENCIA A ESE NOMBRE EN CUALQUIER MOMENTO

#Funcion para crear un saludo

# def saludo_Secreto():
#     print("HOLA BUENAS")
#
#     a = input("¿Como estas?: ")
#     b = input("¿Cuanto es 2 más 2?:"
#               "\nRespuesta:")
#
#     if b == "2":
#         print("Tu si sabesss")
#
#
# #LLAMAR A LA FUNCION  con los 2 parentesis( )
# saludo_Secreto()

#LAS FUNCIONES SE LE PUEDE PASAR PARAMETROS

#FUNCION PARA SALUDO SECTARIO
#PASAR VARIABLES ARGUMENTOS/PARAMETROS A LA FUNCION (NOMBRE DE LA VARIABLE)

# def saludo_sectario(nombre):
#     print("HOLA {} ".format(nombre[::-1]))
#
#
# saludo_sectario("JOSE")
# saludo_sectario("MARIO")
# saludo_sectario("RAMON")

#TAMBIEN PUEDE DEVOLVER EL PARAMETRO/ARGUMENTO NO SOLO RECIBIRLO

# def largo_string(mi_string):
#     largo = 0
#     for i in mi_string:
#         largo += 1
#     # DEVUELVE EL LARGO
#     return largo
#
#
# largo_de_la_string = largo_string("HOLA SEÑORES COMON ESTAID")
# print(largo_de_la_string)


#AHORA LA ESTRUCTURA SERÁ ASI PARA TODOD LOS PROYECTOS
#PROGRAMACION FUNCIONAL
def main():
    print("HOLA MUNOD")

#CONVENCION PARA EJECUTAR EL MAIN PUEDE SER
if __name__ == "__main__":
    main()