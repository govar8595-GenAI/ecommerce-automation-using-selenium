# 🛒 E-commerce Automation using Selenium

## 📌 Project Overview

This project automates an end-to-end e-commerce workflow using Selenium WebDriver with Python.

The automation simulates a real user performing:

- Login  
- Product sorting  
- Adding product to cart  
- Cart validation  
- Checkout process  
- Order completion  

The framework is built using the Page Object Model (POM) design pattern to ensure scalability, maintainability, and clean separation of test logic.

---

## 🚀 Features Automated

- ✅ User Login  
- ✅ Product Sorting (Low to High)  
- ✅ Add Product to Cart  
- ✅ Cart Validation  
- ✅ Checkout Flow  
- ✅ Order Confirmation  
- ✅ Screenshot Capture on Successful Order  

---

## 🏗 Project Structure

ecommerce-automation-using-selenium/

│  
├── driver_setup.py  
├── main.py  
├── pages/  
│   ├── login_page.py  
│   ├── products_page.py  
│   ├── cart_page.py  
│   └── checkout_page.py  
│  
└── screenshots/  

---

## 🧠 Technologies Used

- Python 3  
- Selenium WebDriver  
- WebDriverWait (Explicit Waits)  
- ChromeDriver  
- webdriver-manager  
- Page Object Model (POM)  

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/govar8595-GenAI/ecommerce-automation-using-selenium.git  
cd ecommerce-automation-using-selenium  

---

### 2️⃣ Create Virtual Environment

python -m venv .venv  
source .venv/bin/activate  

(Windows users: .venv\Scripts\activate)

---

### 3️⃣ Install Dependencies

pip install selenium webdriver-manager  

---

### 4️⃣ Run the Automation Script

python main.py  

---

## 📸 Output

After successful execution:

- The order is completed successfully  
- A screenshot is saved inside the screenshots folder  
- The browser closes automatically  

---

## 🎯 Learning Outcomes

Through this project:

- Implemented Page Object Model (POM) architecture  
- Used Explicit Waits for stable automation  
- Handled Chrome password manager popup interference  
- Built modular and scalable test framework  
- Practiced real-world debugging techniques  

---

## 🔍 Why Page Object Model?

Page Object Model improves:

- Code readability  
- Reusability  
- Maintainability  
- Scalability of automation scripts  

Each page has its own class, keeping test logic clean and organized.

---

## 👨‍💻 Author

Govardhan  
Batch 6 – Week 1 Selenium Assignment  
GitHub: https://github.com/govar8595-GenAI  