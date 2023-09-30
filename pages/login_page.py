from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='email']")  
        self.password_input = (By.ID, 'outlined-adornment-password')  
        self.login_button = (By.XPATH, "//button[text()='Iniciar sessão']")
    
    def navigate_to_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.submit()

