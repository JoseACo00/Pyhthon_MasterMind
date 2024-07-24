from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service


#ES BOTS QUE SON PENDIENTES DE ALGO ENTRADA LIMITADA CUANDO BAJE DE PRECIO O ALGO QUE QUIERES
#INSTALAR UN PAQUETE REQUEST  y pip install requests-html
# #VAMOS A UTILIZAR CELENIUM PARA EL BOT QUE COMPRE EL PRODUCTO
# driver = webdriver.Firefox()

#Ruta del producto que se busca comprar o sea lo ques se
url_product = "https://www.coolmod.com/nano-cable-usb-2-0-3a-tipo-usb-c-m-am-2m-negro/"

def seach_id_of_page(request):
    id_of_html=input("Dime la etiqueta para buscar y si hay stock"
                     "\nEtiqueda: ")

    where_buy = request.html.find("#"+id_of_html)

    looking_for_stock(where_buy)
    # return where_buy

def looking_for_stock (where_buy):
    # SI TINE ALGO ES QUE EXISTE EL BOTON DE COMPRA
    if len(where_buy) > 0:
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url_product)
        sleep(1)
        driver.find_element(By.CLASS_NAME, "CybotCookiebotDialogBodyButton").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-circle-xmark.close-icon").click()
        sleep(1)
        # driver.find_element(By.CSS_SELECTOR, ".up.button.w-100").click()
        driver.find_element(By.XPATH, "/html/body/main/div[3]/div[4]/div[3]/div/div/div[3]/div[2]/button[1]").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".swal2-styled.swal2-confirm").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".button.d-block").click()

        #COGER LOS INPUTS DE CORREO Y PASSWORD Y ESCRIBIR
        form = driver.find_element(By.ID, "form-login")

        email = form.find_element(By.NAME, "user-email")
        password = form.find_element(By.NAME, "user-password")

        email.send_keys("JOSELEPURBEA@GMAIL.COM")
        password.send_keys("HOLALITAS12")
        sleep(0.2)
        driver.find_element(By.ID, "btn-login").click()
    else:
        print("NO ESTA DISPONIBLE EL PRODUCTO TODAVIA")


def main():

    session = HTMLSession()
    request = session.get(url_product)
    seach_id_of_page(request)
    #ID de una etiqueta
    # id_of_html = "#spinnerbuybuttoncontainer"




if __name__ == '__main__':
    main()





# CREEAR SESSION
# session = HTMLSession()
# HACER QUE SE REPITA HASTA QUE HAYA STOCK
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
# sleep para que haga la peticion para que no sature las diferentes peticiones
# sleep(5)


def search_product_of_pcComponente(url_product):
    session = HTMLSession()

    name_id = input("Dime el nombre de la etiqueta para saber si está en el HTML ")
    while True:
        request = session.get(url_product)

        id_of_html = request.html.find("#" + name_id)

        if len(id_of_html) > 0:
            print("Hay stock")
            break
        else:
            print("No hay stock")

        sleep(5)