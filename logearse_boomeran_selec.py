
#NO TIENE ID    - SELECTORES
#credenciales: ingresar manualmente

import time
import getpass
from selenium import webdriver


#def_variables_selectores
url = 'https://www.bumeran.com.pe/'
boton_iniciar_sesion = '#root > div > div.sc-bmyXtO.hszyRB > div > div > div > div > div > div > ul > li.sc-TOsTZ.sc-iBEsjs.DWySv > a'
ingresar_mail = '#email'
ingresar_pass = '#password'
boton_ingresar = '#form-signin > div.sc-kkbgRg.fdJgbu > button'

user = input("ingrese correo: ")
password = getpass.getpass()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)
 
#selectores
try:
    driver.find_element_by_css_selector(boton_iniciar_sesion).click()
    time.sleep(1)
    driver.find_element_by_css_selector(ingresar_mail).send_keys(user)
    time.sleep(1)
    driver.find_element_by_css_selector(ingresar_pass).send_keys(password)
    time.sleep(2)
    driver.find_element_by_css_selector(boton_ingresar).click()
    
    time.sleep(10)
    driver.quit()
    print("Proceso terminado papi")

except:
    print("el proceso falló pipipi")


