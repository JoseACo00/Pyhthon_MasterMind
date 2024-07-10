#1EJERCICIO DE FUNCIONES
#Usando la nueva estructura de programas basado en la función main() y la condición if final,
# crea un programa de cualquier tipo. Lo que te de la gana. Usa el debugger para ver como se produce el hilo de ejecución del código.

# def main():
#     print("VAMOS A REALIZAR UNA CALCUALDORA")
#     number1= int(input("Ingrese un numero 1: "))
#     number2= int(input("Ingrese un numero 2: "))
#
#     print("ACCIONES PARA LA CALCULDAORA")
#     print("\nA:SUMA"
#           "\nB:RESTA"
#           "\nC:SUMA"
#           "\nD:DIVISION")
#     accionn = input("Respuesta:")
#
#     if accionn == "A":
#         respuesta = number1 + number2
#         print(respuesta)
#     elif accionn == "B":
#         respuesta = number1 - number2
#         print(respuesta)
#     elif accionn == "C":
#         respuesta = number1 * number2
#         print(respuesta)
#     elif accionn == "D":
#         respuesta = number1 / number2
#         print(respuesta)
#
#
#
# if __name__ == "__main__":
#     main()


#Ejercicio 2
#Crea un programa que contenga una función que calcule la potencia de un numero introducido como argumento, por ejemplo
# print(potencia(3))
#
# > 9
#
# print(potencia(5))
#
# > 25

def main(base, exponente):

    print("Vamosa a calcular la potencia")
    # base = int(input("Ingresa la base: "))
    # exponente = int(input("Ingresa el exponente: "))
    calculo = base**exponente
    print("LA POTENCIA DE BASE: {} Y EXPONENTE: {} "
          "\nES:{}".format(base, exponente, calculo))



if __name__ == '__main__':
    main(2,3)