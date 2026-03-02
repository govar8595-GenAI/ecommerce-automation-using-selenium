import time
from driver_setup import get_driver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

print("===== E-COMMERCE AUTOMATION STARTED =====")

driver = get_driver()

# Login
login = LoginPage(driver)
login.load()
time.sleep(3)

login.login("standard_user", "secret_sauce")
time.sleep(3)

# Products
products = ProductsPage(driver)
products.sort_low_to_high()
time.sleep(3)

products.add_first_product_to_cart()
time.sleep(3)

products.go_to_cart()
time.sleep(3)

# Cart
cart = CartPage(driver)
cart.verify_cart_count()
time.sleep(2)

cart.checkout()
time.sleep(5)

# Checkout
checkout = CheckoutPage(driver)
checkout.fill_details("Govardhan", "K", "600001")
time.sleep(3)

checkout.finish_order()
time.sleep(3)

checkout.verify_success()

driver.save_screenshot("screenshots/order_success.png")

print("===== ORDER COMPLETED SUCCESSFULLY =====")

time.sleep(3)
driver.quit()