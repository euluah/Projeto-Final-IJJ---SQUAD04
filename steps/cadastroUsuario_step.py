from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.cadastroUsuario_page import CadastroUsuarioPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from time import sleep


@given(u'que estou na página inicial')
def go_to_page(context):
    context.cadastroUsuario_page = CadastroUsuarioPage(context.browser)  # Crie uma instância da página inicial
    context.browser.get("https://projetofinal.jogajuntoinstituto.org")


@when(u'eu clicar no link “Clique aqui e registre-se”')
def step_impl(context):
    sleep(7)
    link_registro = context.browser.find_element(By.XPATH, "//a[contains(text(), 'Clique aqui e registre-se')]")
    link_registro.click()

@when(u'preencher os campos necessários')
def step_impl(context):
   faker = Faker('pt_br')
   email = faker.email()
   context.cadastroUsuario_page.enter_email(email)
   context.cadastroUsuario_page.enter_senha("22210628")
   context.cadastroUsuario_page.confirmar_senha("22210628")
   
   


@when(u'clicar no botão “Criar conta”')
def step_impl(context):
    context.cadastroUsuario_page.click_criar_conta_button()


@then(u'deve-se exibir a mensagem “Usuário cadastrado com sucesso”')
def step_impl(context):
    texto_esperado = "Usuário cadastrado com sucesso"
    try:
        # Espera até que o texto seja visível na página
        WebDriverWait(context.browser, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//*"), texto_esperado)
        )
        assert True, f"O texto '{texto_esperado}' está visível na página."
    except AssertionError:
        assert False, f"O texto '{texto_esperado}' não está visível na página."
