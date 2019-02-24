from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class pelogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Programming\chromedriver.exe')
    def test_login(self):
        driver = self.driver
        driver.get('https://www.pythonanywhere.com/login/')
        login = driver.find_element(By.ID,'id_auth-username')  ##Логин
        login.send_keys('741852')
        pswrd = driver.find_element(By.ID,'id_auth-password')  ## Пароль
        pswrd.send_keys('Gena250394')
        auth = driver.find_element(By.XPATH,'//*[@id="id_next"]')  ##Тыкаем войти
        auth.click()
        if driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/h1/small').text == "Welcome back, 741852": ##Проверяем что вход удался
            print ('Ништяк')
        else:
            print ('Шеф, все пропало!')
        driver.quit()