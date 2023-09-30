from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.cadasproProduto_page import CadastroProdutoPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

@given(u'que o vendedor está logado no site e acessa a página de cadastro de produto')
def go_to_page(context):
    context.cadastroProduto_page = CadastroProdutoPage(context.browser)  # Crie uma instância da página inicial
    context.browser.get("https://projetofinal.jogajuntoinstituto.org")
    context.cadastroProduto_page.enter_username("euluah@gmail.com")
    context.cadastroProduto_page.enter_password("22210628")
    context.cadastroProduto_page.click_login_button()

    

@when(u'o vendedor preenche os campos obrigatórios com informações válidas e clica no botão "Cadastrar Produto"')
def step_impl(context):
    context.cadastroProduto_page.click_add_product_button()
    context.cadastroProduto_page.enter_product_name("camisa")
    context.cadastroProduto_page.enter_product_description("amarela")
    context.cadastroProduto_page.select_product_category("Roupas")
    context.cadastroProduto_page.enter_product_price("34.99")
    context.cadastroProduto_page.upload_product_image('/Users/imacruz/Downloads/calopsita-pode-tomar-cafe.jpeg')
    context.cadastroProduto_page.enter_product_shipment_info("19.90")
    context.cadastroProduto_page.click_save_product_button()

@then(u'o produto é registrado com sucesso e uma mensagem de confirmação é exibida')
def step_impl(context):
    texto_esperado = "Produto enviado com sucesso!!"
    try:
        # Espera até que o texto seja visível na página
        WebDriverWait(context.browser, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*"), texto_esperado)
        )
        assert True, f"O texto '{texto_esperado}' está visível na página."
    except AssertionError:
        assert False, f"O texto '{texto_esperado}' não está visível na página."
