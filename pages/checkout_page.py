from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_details(self, first, last, postal):

        # Wait until correct page
        self.wait.until(EC.url_contains("checkout-step-one"))

        # Wait until field is visible
        first_name = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )

        # Scroll into view (important for Mac sometimes)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_name)

        # Small pause to ensure stable interaction
        self.wait.until(EC.element_to_be_clickable((By.ID, "first-name")))

        first_name.clear()
        first_name.send_keys(first)

        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )

        continue_btn.click()

        # Wait for next step
        self.wait.until(EC.url_contains("checkout-step-two"))

    def finish_order(self):

        finish_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )

        finish_btn.click()

        self.wait.until(EC.url_contains("checkout-complete"))

    def verify_success(self):

        message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )

        assert "Thank you for your order!" in message.text