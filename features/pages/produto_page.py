from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .Elements.produto_page_elements import *
from .base_page import *


class ProdutoPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def verificarTitulo(self, context):
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((TITULO_PRODUTO[0], TITULO_PRODUTO[1])))
        return context.driver.find_element(TITULO_PRODUTO[0], TITULO_PRODUTO[1]).text

    def verificarPreco(self, context):
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((PRECO_PRODUTO[0], PRECO_PRODUTO[1])))
        return context.driver.find_element(PRECO_PRODUTO[0], PRECO_PRODUTO[1]).text
