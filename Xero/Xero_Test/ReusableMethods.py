from selenium.common.exceptions import NoSuchElementException


class Reusable_Methods:


    @staticmethod
    def compare(text1, text2, element):
        if (text1 == text2 or (text1 in text2) or (text2 in text1)):
            print(element, " is displayed")
            assert True
        else:

            print(element, " is not displayed")
            assert False

    @staticmethod
    def Click(element,obj):
        if(element.is_displayed()):
            print(obj," is found")
            element.click()
            assert True
        else:
            print(obj, " is not found")
            assert False

    @staticmethod
    def EnterText(element,text,obj):
        if (element.is_displayed()):
            print(obj, " is found")
            element.send_keys(text)
            assert True
        else:
            print(obj, " is not found")
            assert False

    @staticmethod
    def exists(element,obj):

        if(element):
                print(obj," exists")
        else:
            print(obj," does not exist")







