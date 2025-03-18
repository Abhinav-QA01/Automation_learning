class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def find(self,*locator):
        return self.driver.find_element(*locator)