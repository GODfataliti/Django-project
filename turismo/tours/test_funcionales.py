from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv

CHROMEDRIVER_PATH = os.getenv('DRIVERCHROME_PATH')

class TourViewsFuncionalTestCase(LiveServerTestCase):
    def setUp(self):
        options=Options()
        #options.headless=True
        options.add_argument("--window-size=1920,1080")
        self.driver=webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,options=options)
    
    def test_home(self):
        driver=self.driver
        driver.get('http://localhost:8000/')
        self.assertEqual(driver.title,"Gestion Turistica")
        assert 'Bienvenido al Sistema de Turismo' in driver.page_source
    
    def test_testpagina(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.set_window_size(1063, 708)
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.find_element(By.ID, "navbarNav").click()
        self.driver.find_element(By.CSS_SELECTOR, ".footer-copyright").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
        self.driver.find_element(By.LINK_TEXT, "Ir").click()
        self.driver.find_element(By.LINK_TEXT, "Borrar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".active > .nav-link").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.find_element(By.CSS_SELECTOR, "html").click()
    
    def tearDown(self):
        self.driver.quit()