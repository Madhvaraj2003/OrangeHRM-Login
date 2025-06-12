# Imported  all the required Modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
# Locators for login page elements
        self.username_input = (By.NAME, "username") # username input field
        self.password_input = (By.NAME, "password") # password input field
        self.login_button = (By.XPATH, "//button[@type='submit']") # Login button
        self.profile_icon = (By.XPATH, "//img[@alt='profile picture']") # Post login dashboars element
        
        
    def open_url(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
# Sending the needed elements to webdirver        
        WebDriverWait(self.driver, 10). until(EC.presence_of_element_located(self.username_input)).send_keys(username)   
        WebDriverWait(self.driver, 10). until(EC.presence_of_element_located(self.password_input)).send_keys(password)   
        WebDriverWait(self.driver, 10). until(EC.element_to_be_clickable(self.login_button)).click()


        
# Function for successful login
    def is_login_sucessful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.profile_icon))
            print("login sucessful, profile icon found")
            return True
        except:
            print("Login was unsuccessful")
            return False
