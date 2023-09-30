from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CadastroProdutoPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@name='email']")  
        self.password_input = (By.ID, 'outlined-adornment-password')  
        self.login_button = (By.XPATH, "//button[text()='Iniciar sessão']")
        self.addProduct_button = (By.CSS_SELECTOR, "button[type='button'][aria-haspopup='dialog']")
        self.nameProduct_input = (By.NAME,"name")
        self.descriptonProduct_input = (By.NAME,"description")
        self.categoryProduct_button = (By.XPATH,"//span[normalize-space()='Roupas']")
        self.priceProduct_input = (By.NAME,"price")
        self.imageProduct_input = (By.NAME,"image")
        self.shipmentProduct_input = (By.NAME,"shipment")
        self.saveProduct_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def click_add_product_button(self):
        add_product_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.addProduct_button)
        )
        add_product_button.click()

    def enter_product_name(self, product_name):
        product_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.nameProduct_input)
        )
        product_name_field.send_keys(product_name)

    def enter_product_description(self, product_description):
        product_description_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.descriptonProduct_input)
        )
        product_description_field.send_keys(product_description)

    def select_product_category(self, category_name):
        category_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.categoryProduct_button)
        )
        category_button.click()

        category_option_locator = (By.XPATH, f"//span[normalize-space()='{category_name}']")
        category_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(category_option_locator)
        )
        category_option.click()

    def enter_product_price(self, product_price):
        product_price_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.priceProduct_input)
        )
        product_price_field.send_keys(product_price)

    def upload_product_image(self, image_path):
        image_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.imageProduct_input)
        )
        image_field.send_keys(image_path)

    def enter_product_shipment_info(self, shipment_info):
        shipment_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.shipmentProduct_input)
        )
        shipment_field.send_keys(shipment_info)

    def click_save_product_button(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.saveProduct_button)
        )
        save_button.click()

       
        
        
       

        