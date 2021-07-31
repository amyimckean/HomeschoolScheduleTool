from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Create your tests here.
class APPLETests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def testText(self):
        self.selenium.get('http://127.0.0.1:8000/')
        assert 'APPLE' in self.selenium.page_source

    def testNoText(self):
        self.selenium.get('http://127.0.0.1:8000/')
        assert 'amy' not in self.selenium.page_source


