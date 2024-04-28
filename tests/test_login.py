import unittest
from utils.webdriver import WebDriver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_successful_login(self):
        # Test login functionality
        self.login_page.login(username="testuser", password="password")
        # Assert login success or perform other validation
