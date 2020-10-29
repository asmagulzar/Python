from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import *



class Reusable_Methods:

    # @staticmethod
    # def Initialize():
    #     path = r"C:\Users\mehraj.g\.m2\repository\webdriver\chromedriver\win32\86.0.4240.22\chromedriver.exe"
    #     driver = webdriver.Chrome(path)
    #     driver.maximize_window()


    @staticmethod
    def compare(text1,text2,element):
        if (text1 == text2 or (text1 in text2) or (text2 in text1)):
            print(element," is displayed")
            return True
        else:
            print(element, " is not displayed")
            return False



