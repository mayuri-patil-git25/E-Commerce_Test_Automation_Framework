# 📦AutomationExercise E-Commerce Testing Framework

An automated end-to-end testing framework for the [AutomationExercise](https://automationexercise.com/) demo e-commerce website build using **python**, **selenium** and **unittest**.
This framework is designed for practicing real world automation testing workflows following industry-standard **Page Object Model (POM)** architecture.

## ✨ Features
- Automated product purchase flow with quantity and address verification
- Organized code structure using **Page Object Model (POM)**
- Explicit wait mechanism for reliable element interactions
- Externalized sensitive data using `.env` variables
- Clean, modular, and scalable project layout

## 🛠️ Tech Stack
- **Python**
- **Selenium WebDriver**
- **unittest** (Python’s built-in testing framework)
- **python-dotenv** (for environment variables)

## 📋 Prerequisites
- Python installed 

- Google Chrome installed

- ChromeDriver installed and path set (or managed via webdriver-manager if applicable)

## 🚀 How to Set Up and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/mayuri-patil-git25/AutomationExercise_E-Commerce_Testing.git
   cd AutomationExercise_E-Commerce_Testing
   
2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    .venv\Scripts\activate

3. Activate the virtual environment: 
- On Windows
    ```bash
    .venv\Scripts\activate
- On Mac/Linux
  ```bash
  source .venv/bin/activate
  
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt
   
5. Create a .env file in the project root and add:
    ```bash
    EMAIL=your_email@example.com
    PASSWORD=your_password
    EXPECTED_ADDRESS=Your expected address 
   
6. Run the test:
    ```bash
   python tests/test_order_flow.py
   
## 📌 Notes:
-Make sure your Chrome version matches your ChromeDrive version.

-This project is for practice and learning purposes on a dummy website.

-Never push real credentials to GitHub — always use .env for environment variables.

## 👩‍💻 Author
**Mayuri Patil**

[GitHub Profile](https://github.com/mayuri-patil-git25)