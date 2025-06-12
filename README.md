# OrangeHRM-Login
 Automated login testing for the OrangeHRM portal using Python, Selenium, Pytest, Page Object Model (POM), and Data-Driven Testing with Excel integration.

This project automates the login functionality testing of the OrangeHRM demo portal using Python, Selenium, Pytest, and the Page Object Model (POM) design pattern. It implements Data-Driven Testing (DDT) by reading multiple login test cases from an Excel sheet and writing the results back to the same file.


---

📁 Project Structure

OrangeHRM_Login_Automation/
├── Page/                    # Page Object Models (LoginPage)
├── Tests/                   # Test scripts using Pytest
├── Test-data/              # Excel file with login data
├── conftest.py             # Pytest fixture for WebDriver setup
├── README.md               # Project documentation


---

✅ Features

Automates login for multiple user credentials.

Uses POM for clean and maintainable code.

Reads test data (username, password, expected result) from Excel.

Writes actual results (pass/fail) back to Excel.

Supports test parameterization with pytest.mark.parametrize.

Generates test reports via Pytest plugins like HTML reports or Allure.



---

🛠️ Technologies Used

Python 3

Selenium WebDriver

Pytest

OpenPyXL (for Excel handling)

POM (Page Object Model)
