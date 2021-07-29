from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TourViewsFuncionalTestCase(LiveServerTestCase):
    def setUp(self):
        options=Options()
        options.headless=True
        options.add_argument("--window-size=1920,1080")
        self.driver=webdriver.Chrome(options=options)
    
    def test_home(self):
        driver=self.driver
        driver.get('http://localhost:8000/')
        self.assertEqual(driver.title,"Gestion Turistica")
        assert 'Bienvenido al Sistema de Turismo' in driver.page_source
    
    def tearDown(self):
        self.driver.quit()