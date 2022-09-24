from behave import given, when, then


@given(u'que acesso o site da amazon')
def acesso_o_site_da_amazon(context):
    context.home_page.abrir_page(context)


@when(u'busco por {produto} e pressiono Enter')
def busco_produto(context, produto):
    context.home_page.digitar_texto(context, produto)
    context.home_page.clicar_enter(context)


@then(u'exibe uma lista de produtos relacionados com {produto}')
def exibe_uma_lista(context, produto):
    context.lista_page.verficar_texto_resultado(context, produto)


@when(u'escolho {titulo}')
def escolho_produto(context, titulo):
    if context.lista_page.escolho_titulo(context, titulo):
        assert True
    else:
        assert False  , "Não encontrei o titulo : {}".format(titulo)


@then(u'aparece {titulo} no valor de {preco}')
def aparece_titulo_e_calor(context, titulo, preco):
    assert titulo == context.produto_page.verificarTitulo(context), "\ntítulo esperado: {} \ntitulo recebido: {}\n".format(
        titulo, context.produto_page.verificarTitulo(context))
    assert preco == context.produto_page.verificarPreco(context), "\npreco esperado: {} \npreco recebido: {}\n".format(
        preco, context.produto_page.verificarPreco(context))
