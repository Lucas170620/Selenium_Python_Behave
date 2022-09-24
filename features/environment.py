from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.pages.base_page import BasePage
from features.pages.home_page import HomePage
from features.pages.lista_page import ListaPage
from features.pages.produto_page import ProdutoPage


def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    base = BasePage(context.driver)
    context.home_page = HomePage(base)
    context.lista_page = ListaPage(base)
    context.produto_page= ProdutoPage(base)


def before_scenario(context, scenario):
    context.driver.maximize_window()


def before_step(context, step):
    context.driver.implicitly_wait(7)
