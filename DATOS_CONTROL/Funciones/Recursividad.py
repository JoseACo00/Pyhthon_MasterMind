#Funciones recursivas
#from time import sleep

# def c():
#     print('C')
#     sleep(1)
#     a()
# def b():
#     print('B')
#     sleep(1)
#     c()
# def a():
#     print('A')
#     sleep(1)
#     b()

# def main():
#     a()
#     #pass #SE PONE CUANDO NO QUIERES PONER NADA Y AUN ASÍ QUIERES QUE SE EJECUTE
#
# if __name__ == '__main__':
#     main()

# def sumar_uno(a):
#     print(a)
#     a += 1
#     if a != 100:
#         sumar_uno(a)


#SECUENCIA DE FIBONACCI

#PODEMOS HACER QUE LA FUNCIONES TENGA DISTINTAS SET DE PARAMETROS PASABLES (LISTA O ITERRABLE)

def medir_largo(iterable, *args, sumar_todo=False): #ES ATRIBUTOS OPCIONALES COMO sumar_todo  ARGUMENTO OPCIONAL
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)


def main():
    print(medir_largo("hola"))
    print(medir_largo("Holadads", "COMO ESTAS"))

if __name__ == '__main__':
    main()