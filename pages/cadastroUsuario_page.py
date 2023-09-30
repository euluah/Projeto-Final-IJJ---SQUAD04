from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CadastroUsuarioPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, "email")
        self.senha_input = (By.NAME, "password")
        self.confirmar_senha_input = (By.NAME, "confirmPassword")
        self.criar_conta_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_input)
        )
        email_field.send_keys(email)

    def enter_senha(self, senha):
        senha_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.senha_input)
        )
        senha_field.send_keys(senha)

    def confirmar_senha(self, senha):
        confirmar_senha_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.confirmar_senha_input)
        )
        confirmar_senha_field.send_keys(senha)

    def click_criar_conta_button(self):
        criar_conta_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.criar_conta_button)
        )
        criar_conta_button.submit()