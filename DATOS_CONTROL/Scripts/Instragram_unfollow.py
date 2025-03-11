from time import sleep
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.common.by import By

#VAMOS A CREEAR UN SCRIPT PARA PODER ELIMINAR GENTE QUE SIGUES POR ERROR O QIERES DEJAR DE SEGUIR RÁPIDAMENTE

url_instagram = "https://www.instagram.com/"


def instagram_account():

    user_of_instagram=input("Dime el nombre de tu cuenta de instagram"
                            + "\nUSER: ")
    password_of_instagram=input("DIME AHORA TU PASSWORD: "
                                +"\nPASSWORD: ")

    return user_of_instagram, password_of_instagram

def show(user_of_instagram, password_of_instagram):
    print("Usuario:", user_of_instagram)
    print("Contraseña:", password_of_instagram)

def login_instagram(user, passworde):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url_instagram)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button._a9--:nth-child(2)").click()
    sleep(1)

    #INPUTS EN EL LOGGIN
    form_account = driver.find_element(By.ID, "loginForm")

    email = form_account.find_element(By.NAME, "username")
    password = form_account.find_element(By.NAME, "password")

    email.send_keys(user)
    password.send_keys(passworde)
    sleep(0.4)
    driver.find_element(By.CSS_SELECTOR, "._acap").click()



def main():
    session = HTMLSession()
    request = session.get(url_instagram)

    #Llama a la función y guarda los valores retornados
    user, password = instagram_account()


    # # Pasa los valores obtenidos a la función show
    # show(user, password)

    login_instagram(user, password)

if __name__ == '__main__':
        main()
