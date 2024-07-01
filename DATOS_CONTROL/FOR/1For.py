#VAMOS  A EMPEZAR CON EL FOR PARA SABER COMO FUNCIONA Y SE UTILIZA

#1

#LISTA DE 1 A 10
a = [1,2,3,4,5,6,7,8,9,10]
vocales = ['a','e','i','o','u', 'A','E','I','O','U']

vocales_Encontradas = 0
#LEER CADA POSICION DE DEL ARRAY/LISTA
#for item  in a:
 #   print(item)

#2
frase = "HOLA HOY ESTOY APRENDIENDO PYTHON"
#for letra in frase:
 #   print(letra)

 #3 BUSCAR LAS VOCALES EN UN FRASE
for letra in frase:
     if letra in vocales:
         print("HE ENCONTRADO UNA '{}'".format(letra))
         vocales_Encontradas += 1

print("EL NÚMERO DE VOCALES ENCONTRADAS FUERON DE: {}".format(vocales_Encontradas))