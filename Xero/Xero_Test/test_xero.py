from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Xero_Test.ReusableMethods import Reusable_Methods
from selenium.webdriver.common.keys import Keys
import allure
import time
import pytest
import logging
import sys





class Test_Xero():
    # global logger
    # logging.basicConfig(level=logging.DEBUG)
    # logger = logging.getLogger()


    @pytest.fixture(scope='class')
    def test_SetUp(self):
        print("Setup")
        path = r"C:\Users\mehraj.g\.m2\repository\webdriver\chromedriver\win32\86.0.4240.22\chromedriver.exe"
        global driver
        driver = webdriver.Chrome(path)
        driver.maximize_window()
        driver.implicitly_wait(30)
        global wait
        wait = WebDriverWait(driver, 20, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        yield
        driver.quit()


    def test_IncorrectEmail(self,test_SetUp):
        driver.get("https://login.xero.com/")
        Reusable_Methods.compare("Login | Xero Accounting Software", driver.title, "Login Page")
        #logger.info("LOGGED Setup is executed successfully")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sweetyriya@gmail.com")
        driver.find_element_by_id("password").send_keys("Hello123")
        driver.find_element_by_id("submitButton").click()
        time.sleep(5)
        wait = WebDriverWait(driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='x-boxed warning']")))
        errormessage = driver.find_element_by_xpath("//div[@class='x-boxed warning']").text
        print(errormessage)
        Reusable_Methods.compare(errormessage, "Your email or password is incorrect", "Error Message")
        #  logger.error("LOGGED Error message")
        #print("Error Message",file = sys.stderr)

    def test_IncorrectPassword(self):
        driver.get("https://login.xero.com/")
        Reusable_Methods.compare("Login | Xero Accounting Software", driver.title, "Login Page")
        #logger.info("LOGGED Setup is executed successfully")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sweetyriya777@gmail.com")
        driver.find_element_by_id("password").send_keys("123")
        driver.find_element_by_id("submitButton").click()
        time.sleep(5)
        wait = WebDriverWait(driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='x-boxed warning']")))
        errormessage = driver.find_element_by_xpath("//div[@class='x-boxed warning']").text
        Reusable_Methods.compare(errormessage, "Your email or password is incorrect", "Error Message")

    def test_ForgotPassword(self):
        driver.get("https://login.xero.com/")
        Reusable_Methods.compare("Login | Xero Accounting Software", driver.title, "Login Page")
        #logger.info("LOGGED Setup is executed successfully")
        driver.find_element_by_class_name("forgot-password-advert").click()
        Reusable_Methods.compare(driver.title,"Forgotten Password","Forgot Password Page")
        driver.find_element_by_id("UserName").send_keys("sweetyriya777@gmail.com")
        driver.find_element_by_id("submitButton").click()
        pwdresetmsg = driver.find_element_by_xpath("//div[@class='x-boxed noBorder']/p[1]").text
        Reusable_Methods.compare(pwdresetmsg,"A link to reset your password has been sent to:","Password Reset Message")
        Reusable_Methods.compare(pwdresetmsg,"sweetyriya777@gmail.com","Correct Email")




    @pytest.fixture()
    def test_LoginToXero(self,test_SetUp):

        driver.get("https://login.xero.com/")
        Reusable_Methods.compare("Login | Xero Accounting Software", driver.title, "Login Page")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("sweetyriya.777@gmail.com")
        driver.find_element_by_id("password").send_keys("Hello123")
        driver.find_element_by_id("submitButton").click()
        Reusable_Methods.compare("Xero | Dashboard",driver.title,"Xero Dashboard page")

    def test_AllTabs(self,test_LoginToXero):
        Reusable_Methods.compare(driver.find_element_by_xpath("//span[@class='xrh-banner--text xrh-banner--text-center']").text,"You’re on a free 30-day trial that includes all features.","Free Trial Account Banner")

        Reusable_Methods.Click(driver.find_element_by_xpath("//button[@name='navigation-menu/accounting']"),"Accounting Button")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='xrh-dropdown-layout xrh-nav--dropdown xrh-dropdown-is-open xrh-dropdown-is-opening xrh-dropdown-positionleft']")))

        try:
            if(driver.find_element_by_css_selector("ol.xrh-tabgroup.xrh-tabgroup-layout.xrh-navigation.xrh-header-background-color > li:nth-child(3) > div.xrh-dropdown-layout.xrh-nav--dropdown.xrh-dropdown-is-open.xrh-dropdown-is-opening.xrh-dropdown-positionleft").is_displayed()):
                print("Accounting dropdown is displayed")
        except NoSuchElementException:
            print("Accounting Dropdown does not exist")

        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-tabgroup.xrh-tabgroup-layout.xrh-navigation.xrh-header-background-color > li:nth-child(3) > div > div.xrh-dropdown--panel > div > ol:nth-child(1) > li:nth-child(2) > a"),"Reports Button")
        Reusable_Methods.compare("Xero | Reports",driver.title,"Reports page")
        driver.back()
        Reusable_Methods.Click(driver.find_element_by_name("navigation-menu/contacts"),"Contacts Button")
        Reusable_Methods.exists(driver.find_elements_by_css_selector("ol.xrh-tabgroup.xrh-tabgroup-layout.xrh-navigation.xrh-header-background-color > li:nth-child(4) > div.xrh-dropdown-layout.xrh-nav--dropdown.xrh-dropdown-is-open.xrh-dropdown-is-opening.xrh-dropdown-positionleft"),"Contacts Dropdown")

        try:
            if(driver.find_element_by_css_selector("ol.xrh-tabgroup.xrh-tabgroup-layout.xrh-navigation.xrh-header-background-color > li:nth-child(4) > div.xrh-dropdown-layout.xrh-nav--dropdown.xrh-dropdown-is-open.xrh-dropdown-is-opening.xrh-dropdown-positionleft").is_displayed()):
                print("Contacts dropdown is displayed")
        except NoSuchElementException:
            print("Contacts Dropdown does not exist")

        Reusable_Methods.Click(
            driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(1) > button"),
            "+ Sign button")
        Reusable_Methods.exists(driver.find_elements_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(1) > div.xrh-dropdown-layout.xrh-addon--dropdown.xrh-dropdown-is-open.xrh-dropdown-is-opening.xrh-dropdown-positionright"),"+ Sign Dropdown")
        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(4) > button"),"Help ? Button")
        Reusable_Methods.exists(driver.find_elements_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(4) > button.xrh-button.xrh-addon--iconbutton.xrh-header--iconbutton.xrh-focusable--parent.xrh-focusable--parent-is-active"),"Help ? Dropdown")
        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(3) > button"),"Notification Button")
        Reusable_Methods.exists(driver.find_elements_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(3) > button.xrh-button.xrh-addon--iconbutton.xrh-header--iconbutton.xrh-focusable--parent.xrh-focusable--parent-is-active"),"Notification Dropdown")
        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(2) > button"),"Search Button")
        Reusable_Methods.exists(driver.find_elements_by_css_selector("button.xrh-button.xrh-addon--iconbutton.xrh-header--iconbutton.xrh-focusable--parent.xrh-focusable--parent-is-active"),"Search Dropdown")
        

    def test_UploadProfileImage(self):
        time.sleep(5)
        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(5) > button"),"User Menu Button")
        Reusable_Methods.Click(driver.find_element_by_xpath("//span[contains(text(),'Edit Profile')]"),"Edit Profile")
        time.sleep(5)
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[contains(@id,'button') and @data-automationid='uploadImageButton']"),"Upload Image")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Browse')]")))
        browse=driver.find_element_by_xpath("//div[@class='x-btn x-exclude x-unselectable x-btn-default-small x-noicon x-btn-noicon x-btn-default-small-noicon']//input[@name='file']")
        browse.send_keys("C:/Users/mehraj.g/Downloads/cat.jpg")
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[@class='x-toolbar x-docked x-toolbar-default x-docked-bottom x-toolbar-docked-bottom x-toolbar-default-docked-bottom x-box-layout-ct']//span[@class='x-btn-inner x-btn-inner-center'][contains(text(),'Upload')]"),"Upload")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(@id,'button') and @data-automationid='removeImageButton']")))
        print("Image uploaded")
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[contains(@id,'button') and @data-automationid='removeImageButton']"),"Remove Image Button")
        driver.back()
        time.sleep(5)
        

    def test_LogOut(self):
        Reusable_Methods.Click(driver.find_element_by_css_selector("ol.xrh-addons.xrh-header-background-color > li:nth-child(5) > button"),"User Menu Button")
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[@class='xrh-dropdown-layout xrh-addon--dropdown xrh-dropdown-is-open xrh-dropdown-is-opening xrh-dropdown-positionright']//a[@class='xrh-verticalmenuitem--body'][contains(text(),'Log out')]"),"Logout")


    def test_AddOrg_StdPlan(self,test_LoginToXero):
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[@class='xrh-appmenucontainer']"),"Menu Item")
        parent = driver.current_window_handle
        print(parent)
        Reusable_Methods.Click(driver.find_element_by_xpath("//a[contains(text(),'My Xero')]"),"My Xero")
        driver.switch_to.window(driver.window_handles[1])
        print(driver.current_window_handle)
        Reusable_Methods.exists(driver.find_elements_by_xpath("//h2[contains(text(),'Organizations')]"),"Organization Details")
        Reusable_Methods.Click(driver.find_element_by_xpath("//a[@class='x-btn green']"),"Add an organization Button")
        Reusable_Methods.EnterText(driver.find_element_by_xpath("//input[@class='xui-textinput--input xui-textinput--input-medium']"),"Self","Business name")
        Reusable_Methods.EnterText(driver.find_element_by_xpath("//input[@placeholder='eg: professional services, construction, retail']"),"Testing","Industry")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@class='xui-textinput--input xui-textinput--input-medium']").send_keys(Keys.TAB)
        time.sleep(2)
        Reusable_Methods.Click(driver.find_element_by_xpath("//div[@class='xui-styledcheckboxradio-group']//input[@id = 'Yes']"),"Employees - Yes")
        Reusable_Methods.Click(driver.find_element_by_xpath("//button[contains(text(),'Buy now')]"),"Buy Now Button")
        time.sleep(5)
        driver.close()
        print(driver.current_window_handle)





    @pytest.fixture()
    def test_SignUp(self,test_SetUp):
        driver.get("https://www.xero.com/us/")
        wait = WebDriverWait(driver, 5, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "global-ceiling-bar-cta2")))
        Reusable_Methods.compare("Accounting Software - Do Beautiful Business | Xero US", driver.title, "Xero Page")
        Reusable_Methods.Click(driver.find_element_by_class_name("global-ceiling-bar-cta2"),"Free Trial Button")
        Reusable_Methods.compare("Signup for Xero - Free Trial | Xero US",driver.title,"Free Trial Page")

    def test_SignUp_A(self,test_SignUp):

        Reusable_Methods.EnterText(driver.find_element_by_name("FirstName"),"Asma","First Name")
        Reusable_Methods.EnterText(driver.find_element_by_name("LastName"), "Gulzar", "Last Name")
        Reusable_Methods.EnterText(driver.find_element_by_name("EmailAddress"), "sweety.riya777@gmail.com", "EmailAddress")
        Reusable_Methods.EnterText(driver.find_element_by_name("PhoneNumber"), "5082968534", "PhoneNumber")
        country = Select(driver.find_element_by_name("LocationCode"))
        country.select_by_value("US")
        Reusable_Methods.Click(driver.find_element_by_name("TermsAccepted"),"TermsAccepted")

        '''
        driver.switch_to.frame(0)
        Reusable_Methods.Click(driver.find_element_by_xpath("//*[@id=\"recaptcha-anchor\"]/div[1]"),"recaptcha")
        driver.switch_to.default_content()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
        Reusable_Methods.Click(driver.find_element_by_xpath("//button[@class='btn btn-primary']"),"Get Started Button")
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='message-dynamic text']")))
        Reusable_Methods.compare("Sign up for Xero &amp; Trial Free | Xero | Xero US",driver.title,"Inbox page")
        '''


    def test_SignUp_B(self,test_SignUp):
        Reusable_Methods.Click(driver.find_element_by_css_selector("body.xero.is-live-mode main.main:nth-child(2) div.section.bright.section-padding.section-padding-none.section-bright.section-section_c1c0:nth-child(1) div.row div.small-12.columns form.signup-form.signup-form-no-background div.signup-form-submit.form-group:nth-child(9) > span.g-recaptcha-submit"),"Get Started Button")
        Reusable_Methods.compare(driver.find_element_by_xpath("//span[@id='signup-form-error-message-1']").text,"First name can't be empty","First name can't be empty - error message")
        Reusable_Methods.compare(driver.find_element_by_xpath("//span[@id='signup-form-error-message-2']").text,"Last name can't be empty","Last name can't be empty - error message")
        Reusable_Methods.compare(driver.find_element_by_xpath("//span[@id='signup-form-error-message-3']").text, "Email address can't be empty", "Email address can't be empty - error message")
        color = driver.find_element_by_xpath("//div[@class='form-checkbox']/label").value_of_css_property("color")
        if(color == "rgba(255, 0, 0, 1)"):
            print("Terms and Policy Checkbox is Highlighted")
            assert True
        else:
            print("Terms and Policy Checkbox is not Highlighted")
            assert False


    def test_SignUp_C(self,test_SignUp):
        Reusable_Methods.Click(driver.find_element_by_xpath("//a[contains(text(),'Terms of Use')]"),"Terms Of Use Link")
        Reusable_Methods.compare("Terms of Use | Xero US",driver.title,"Terms of Use page")
        driver.back()
        Reusable_Methods.Click(driver.find_element_by_xpath("//a[contains(text(),'Privacy')]"),"Privacy Link")
        Reusable_Methods.compare("Privacy Notice | Xero US", driver.title, "Privacy page")

    def test_SignUp_D(self, test_SignUp):
        parentwindow = driver.current_window_handle
        print(parentwindow)
        Reusable_Methods.Click(driver.find_element_by_xpath("//a[contains(text(),'offer details')]"),"Offer Details Link")
        driver.switch_to.window(driver.window_handles[2])
        print(driver.window_handles[2])
        Reusable_Methods.compare("Offer details | Xero US", driver.title, "Offer Details page")
































