from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def sort_low_to_high(self):
        dropdown = Select(
            self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container"))
            )
        )
        dropdown.select_by_value("lohi")

    def add_first_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "(//button[text()='Add to cart'])[1]")
            )
        ).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

        self.wait.until(EC.url_contains("cart"))