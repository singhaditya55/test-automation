# 🚀 Automation Testing - Signup & Login (Selenium + Python + Behave)

## 📌 Project Overview
This project automates the **Sign Up & Login** functionality for [Magento Test Website](https://magento.softwaretestingboard.com/) using **Selenium WebDriver**, **Python**, and **Behave (BDD framework)**.

### 🔥 Key Features:
✅ Automated **Sign Up** process.  
✅ Automated **Login** process.  
✅ **Negative test cases** (invalid credentials, existing email, etc.).  
✅ Uses **BDD (Behavior-Driven Development)** with `behave`.  
✅ Implements **Page Object Model (POM)** for structured test scripts.  

---

## 🛠️ Tech Stack:
- **Programming Language:** Python 🐍
- **Automation Framework:** Selenium WebDriver 🚗
- **BDD Framework:** Behave 🌿
- **Assertions:** Python `unittest`
- **Browser:** Chrome (via `chromedriver`)

---

## 📂 Project Structure:
📦 test-automation  
├── 📂 features                # BDD feature files  
│   ├── signup.feature         # Signup test scenarios  
│   ├── login.feature          # Login test scenarios  
│   ├── steps                  # Step definitions for BDD  
│   │   ├── signup_steps.py    
│   │   ├── login_steps.py     
├── 📂 pages                   # Page Object Model (POM) classes  
│   ├── signup_page.py         # Signup page elements & actions  
│   ├── login_page.py          # Login page elements & actions  
├── 📂 reports                 # Test execution reports (screenshots/logs)  
├── 📄 requirements.txt         # Dependencies (Selenium, Behave, etc.)  
├── 📄 Signup_Login_TestCases.xlsx  # Documented test cases  
├── 📄 README.md                # Project documentation  

---

## 🔧 Setup & Installation:

### 1️⃣ Clone the Repository

```git clone https://github.com/yourusername/test-automation.git cd test-automation```


### 2️⃣ Install Dependencies
```pip install -r requirements.txt```

### 3️⃣ Run Tests using Behave
```behave```

Or explicitly run with Python:
```python -m behave```