from selenium import webdriver

class WebDriver:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        # Add support for other browsers as needed

    def quit(self):
        self.driver.quit()
