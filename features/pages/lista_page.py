from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import *
from .Elements.lista_page_elements import *
from selenium.webdriver.support import expected_conditions as EC

class ListaPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.driver)



    def escolho_titulo(self,context,titulo):
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((RESULTADO[0], RESULTADO[1])))
        resultados = context.driver.find_elements(RESULTADO[0],RESULTADO[1])
        for resultado in resultados:
            if resultado.text == titulo:
                resultado.click()
                return True
        return False


    def verficar_texto_resultado(self,context,produto):
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((RESULTADOS_PARA[0],RESULTADOS_PARA[1])))

        resultado = context.driver.find_element(RESULTADOS_PARA[0],RESULTADOS_PARA[1]).text
        product = "\""+produto+"\""

        assert resultado == product
