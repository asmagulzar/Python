import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .ReusableMethods import Reusable_Methods


class Test_Xero(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        #Reusable_Methods.Initialize()
        path = r"C:\Users\mehraj.g\.m2\repository\webdriver\chromedriver\win32\86.0.4240.22\chromedriver.exe"
        cls.driver = webdriver.Chrome(path)
        cls.driver.maximize_window()


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    def test_a_IncorrectEmail(self):
        print("test_IncorrectEmail")
        driver = self.driver
        self.driver.get("https://login.xero.com/")
        self.assertTrue(Reusable_Methods.compare("Login | Xero Accounting Software", self.driver.title, "Login Page"))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sweetyriya77@gmail.com")
        driver.find_element_by_id("password").send_keys("Hello123")
        driver.find_element_by_id("submitButton").click()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

        element = wait.until(EC.visibility_of_element_located(By.XPATH,"//div[@class='x-boxed warning']"))
        errormessage = driver.find_element_by_xpath("//div[@class='x-boxed warning']").text
        self.assertTrue(Reusable_Methods.compare(errormessage,"Your email or password is incorrect","Error Message"))


    def test_c_LoginToXero(self):
        print("test_LoginToXero")
        driver = self.driver
        self.driver.get("https://login.xero.com/")
        self.assertTrue(Reusable_Methods.compare("Login | Xero Accounting Software", self.driver.title, "Login Page"))
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sweetyriya777@gmail.com")
        driver.find_element_by_id("password").send_keys("Hello123")
        driver.find_element_by_id("submitButton").click()
        time.sleep(5)

    def test_b_ForgotPassword(self):
        print("test_ForgotPassword")
        driver = self.driver
        driver.find_element_by_class_name("forgot-password-advert").click()
        self.assertTrue(Reusable_Methods.compare(driver.title,"Forgotten Password","Forgot Password Page"))
        driver.find_element_by_id("UserName").send_keys("sweetyriya777@gmail.com")
        driver.find_element_by_id("submitButton").click()

        #self.assertTrue(Reusable_Methods.compare(pwdresetmsg , "Please check your email","Password Reset Message"))



if __name__ == '__main__':
    unittest.main()
