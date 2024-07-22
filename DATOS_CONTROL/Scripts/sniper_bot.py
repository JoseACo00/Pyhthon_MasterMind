from time import sleep
from requests_html import HTMLSession

#ES BOTS QUE SON PENDIENTES DE ALGO ENTRADA LIMITADA CUANDO BAJE DE PRECIO O ALGO QUE QUIERES
#INSTALAR UN PAQUETE REQUEST  y pip install requests-html

#Ruta del producto que se busca comprar o sea lo ques se
url_product = "https://epomaker.com/products/ajazz-ak820-pro?variant=47007558435124"
# url_product = "https://www.coolmod.com/royal-kludge-rkr87-iso-es-hot-swappable-switch-red-blanco/?gad_source=1&gclid=Cj0KCQjwwO20BhCJARIsAAnTIVRc37A5v55PjM2pv2Jex1D6k9Zcx5ZOY6TBsYXRf2DESc0QR2Rvh3IaAuhoEALw_wcB"




#CREEAR SESSION
# session = HTMLSession()
#HACER QUE SE REPITA HASTA QUE HAYA STOCK
# while True:
#     #HACE LA PETICION A LA URL
#     r = session.get(url_product)
#     #METER EN UN VARIABLE LA ETIQUETA A BSUCAR O ENCONTRAR DE VUELVE UN [] VACIO O CON ELEMENTOS
#     zone_where_buy = r.html.find("#spinnerbuybuttoncontainer")
#     if len(zone_where_buy) > 0:
#         print("Hay stock!!!!!!")
#         break
#     else:
#         print("No hay stock")
    #sleep para que haga la peticion para que no sature las diferentes peticiones
    #sleep(5)




def search_product_of_pcComponente(url_product):
    session = HTMLSession()

    name_id = input("Dime el nombre de la etiqueta para saber si está en el HTML ")
    while True:
        request = session.get(url_product)

        id_of_html = request.html.find("#"+name_id)

        if len(id_of_html) > 0:
            print("Hay stock")
            break
        else:
            print("No hay stock")

        sleep(5)


def main():
    
    search_product_of_pcComponente(url_product)



if __name__ == '__main__':
    main()