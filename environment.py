from selenium.webdriver import Firefox
from behave import fixture, use_fixture
from pages.login_page import Login

def before_scenario(context, scenario):
    context.browser = Firefox()  

def after_scenario(context, scenario):
    context.browser.quit()

# Hook para executar o login antes de cenários específicos



