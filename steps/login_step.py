from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import Login
from time import sleep

@given(u'que eu estou na pagina de login')
def go_to_page(context):
    context.login_page = Login(context.browser)  # Crie uma instância da página de login
    context.browser.get("https://projetofinal.jogajuntoinstituto.org")
    

@when(u'eu informar as minhas credenciais')
def step_impl(context):

    # Use a instância context.login_page para preencher as credenciais de login
    context.login_page.enter_email('euluah@gmail.com')  
    context.login_page.enter_password('22210628')  
    context.login_page.click_login_button()

@then(u'a URL deve ser "https://projetofinal.jogajuntoinstituto.org/products"')
def step_impl(context):
    # Verifique se a URL após o login é a esperada
    sleep(5)
    expected_url = "https://projetofinal.jogajuntoinstituto.org/products"
    current_url = context.browser.current_url
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"