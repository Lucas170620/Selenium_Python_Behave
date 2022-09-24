from selenium.webdriver.common.by import By
from .base_page import *
from .Elements.home_page_elements import *

class HomePage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def digitar_texto(self, context, produto):
        context.driver.find_element(CAMPO_DE_BUSCA[0],CAMPO_DE_BUSCA[1]).send_keys(produto)

    def clicar_enter(self, context):
        context.driver.find_element(BOTAO_DE_BUSCA[0],BOTAO_DE_BUSCA[1]).click()

    def abrir_page(self,context):
        context.driver.get("https://www.amazon.com.br/ref=nav_logo")
