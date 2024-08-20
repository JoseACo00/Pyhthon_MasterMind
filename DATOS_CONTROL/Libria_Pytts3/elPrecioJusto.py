import random

from requests_html import HTMLSession
from speak_and_listen import speak, hear_me
from time import sleep

url_site = "https://www.coolmod.com/"

def main():
    # speak("Bienvenido al precio justo vamos a intentar a divinar los precios de algunos productos")

    session = HTMLSession()

    print("Realizando petición GET a la página principal...")
    main_site = session.get(url_site)
    print(main_site)

    print("Buscando categorías en el sitio principal...")
    categories = main_site.html.find(".subfamilylist ")

    category = random.choice(categories)

    print(category)


if __name__ == '__main__':
    main()


    #subfamilylist