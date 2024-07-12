#1 Ejercicio 1: La secuencia de Fibonacci RECURSIVo
# 1,1,2,3,5,8,13,21

# def fibonacci_recursivo(number):
#
#     if number <= 1:
#         return 1
#
#     return fibonacci_recursivo(number - 1) + fibonacci_recursivo(number - 2)
#
# def main():
#     for a in range(10):
#         print(fibonacci_recursivo(a))


#EJERCICIO2 Potencia con parámetro opcional

def potenciaJose (number, potenciaOpcional = 2):
    print("Vamos a calcular la potencia de un numero")
    calculo = number ** potenciaOpcional
    if  potenciaOpcional != 2:
        print("VAMOS A  CALCULAR LA POTENCIA DE UN NUMERO {} Y BASE {}".format(number, potenciaOpcional))
        print(calculo)
    else:
        print("VAMOS A CALCULAR LA LA POTENCIA DE {}".format(number))
        print(calculo)
def main():
    potenciaJose(5)
    potenciaJose(3, 9)
if __name__ == '__main__':
    main()





