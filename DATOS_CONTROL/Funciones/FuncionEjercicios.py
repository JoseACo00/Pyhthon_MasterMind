#IMPORTS
from random import randint
import string

#1
# La string más larga
# Crea una funcion que reciba una lista de strings como entrada y te diga cual es la más larga de todas
# Ejemplo:
# string_mas_larga("hola", "como", "estas")
# > "estas"

def string_most_bigger():
    palabras = input("Dime palabras que quieras o texto pero separados por comas"
                   "\nWords: " )
    palabranew = palabras.split(",")

    # palabragrande=""
    # wordbigger = 0
    # list_string = []
    # for i in palabranew:
    #     list_string.append(i)
    # print(list_string)

    palabragrande = ""  # Iniciamos con una cadena vacía

    # Iteramos sobre cada palabra en la lista
    for palabra in palabranew:
        # Comparamos la longitud de la palabra actual con la palabra más grande encontrada hasta ahora
        if len(palabra) > len(palabragrande):
            palabragrande = palabra

    # Imprimimos la palabra más grande
    print("La palabra más larga es: {}".format(palabragrande))

    # palabragrande=0
    # for palabra in list_string[1:]:
    #     if palabra > palabragrande:
    #         palabragrande = palabra
    #
    # print("la palabra más grande es: {}" .format(palabragrande))







#2
# Ejercicio 2: Sumando la lista
# Crea una función que sume una lista de números, no se vale usar la función sum()
# Ejemplo:
# suma([1, 2, 3, 4, 5])
# > 15

def sum_of_list():
    numbers = input("DIME LOS NUMEOS SEPARADOS POR COMA PARA CREAR LA LISTA DE NUMEROS")
    list_number = numbers.split(",")

    numbers_list = [int(number) for number in list_number]

    suma = 0

    for number in numbers_list:
        suma += number
        # number = 1
        # suma = suma + number -> suma = 0 + 1 -> suma = 1
        # Segunda
        # iteración:
        # number = 2
        # suma = suma + number -> suma = 1 + 2 -> suma = 3
        # Tercera
        # iteración:
        # number = 3
        # suma = suma + number -> suma = 3 + 3 -> suma = 6
        # Cuarta
        # iteración:
        # number = 4
        # suma = suma + number -> suma = 6 + 4 -> suma = 10
    print(numbers_list)
    print("LA SUMA TOTAL ES : {}".format(suma))






#3
# Ejercicio 3: Par o impar
# Crea una función que te de True como resultado si el número pasado como argumento es impar
# Ejemplo:
# es_impar(3)
# > True
# es_impar(24)
# > False
def par_impar(number):
    print("----------------------"
        "\nExercise 3 (Say is even  o odd /TRUE AND FALSE)")
    if number % 2 == 0:
        print("The number {} is Par:".format(number))
        number = True
        print(number)
    elif number % 2 != 0:
        print("The number {} is Impar:".format(number))
        number = False
        print(number)


#4

# Ejercicio 4: Pregunta algo
# Crea una función que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" dependiendo de si el usuario está seguro.

def sure_or_not():

    print("------------------"
        "\nEXERCISE 4 ")
    answer = input("¿¿Estas seguro??")

    if answer == "yes":
        answer = True
        print(answer)
    elif answer == "no":
        answer = False
        print(answer)
    else:
        print("Options only is yes or no")


#5
# Ejercicio 5: A mayus
# Crea una función que convierta toda una string en mayusculas, no vale usar el método upper()

def convert_to_case(text, case):
    text = input("Dime que frase o string quieres que convierta:"
                   "\nTexto:")

    lower = "abcdefghijklmnopkrstuvwyz "
    upper = "ABCDEFGHIJKLMNOPKRSTUVWYZ "
    res = ''
    for t in text:
        j = 0
        for i in lower:
            if case == "lower":
                if lower[j] == t or upper[j] == t:
                    res += lower[j]
            if case == "upper":
                if lower[j] == t or lower[j] == t:
                    res += upper[j]

            j += 1
    print("TEXTO TO Upper: {}".format(res))
    return res






#6
# Ejercicio 6: Adivina el número
# Crea una función que reciba como argumento un número del 1 al 100 a adivinar y que le pregunte
# al usuario que adivine el número. El código se ejecutará hasta que el usuario adivine.

def guess_number(numberguess):
    number_correct = randint(1,100)
    print(number_correct)
    numberguess = None
    while number_correct != numberguess:
        numberguess = int(input("NUMBER CORRECT: "))
        if numberguess < 0 or numberguess > 100:
            print("ONLY ANSWERS ACCEPTED IS 0 TO 100")

    print("You win the correct number is {}".format(number_correct))


#7
# Ejercicio 7: Lista de la compra
# Crea una función que dada una lista de la compra definida fuera de la función,
# permita al usuario añadir un nuevo item asegurandose que no exista anteriormente en la lista.

list_shopping = ["arroz", "melon", "huevos", "leche"]
def list_shop():

    print("Ejercicio 7")

    terminar = False
    while not terminar:
        new_item = input("Dime que alimento nuevo quieres añadir"
                         "\nAlimento: ")
        if new_item  in list_shopping:
           print("Ese alimento ya esta en la lista sorry")
           print(list_shopping)
           terminar = True

        list_shopping.append(new_item)




#MAIN
def main():

    #  par_impar(14)
    #  sure_or_not()
    # guess_number(0)
    #convert_to_case('a', 'upper')
    #sum_of_list()
    #string_most_bigger()
    list_shop()

if __name__ == '__main__':
    main()