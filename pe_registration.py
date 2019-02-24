import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class peregistration (unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Chrome('D:\Programming\chromedriver.exe')
    def test_login (self):
        driver = self.driver
        driver.get('https://www.pythonanywhere.com/pricing/')
        free = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/ul[1]/li[3]/p/a')  ##Нажимаем на кнопку Create a beginner account
        free.click()
        login = driver.find_element(By.ID,'id_username')  ##Логин
        login.send_keys('741852')
        email = driver.find_element(By.ID,'id_email')  ##Почта
        email.send_keys('ibf64651@zwoho.com')
        pswrd = driver.find_element(By.ID,'id_password1')  ## Пароль
        pswrd.send_keys('Gena250394')
        time.sleep(1) ## Нужно подождать, потому что без задержки поле подтверждения пароля не заполняется
        pswrd2 = driver.find_element(By.ID,'id_password2')  ## Повтор пароля (pswrd=pswrd2)
        pswrd2.send_keys('Gena250394')
        agreebtn = driver.find_element(By.XPATH,'//*[@id="id_tos"]') ##Соглашаемся с правилами сайта
        agreebtn.click()
        register = driver.find_element(By.XPATH,'//*[@id="id_register_button"]')  ##Кнопка регистрации
        register.click()
        endtour = driver.find_element(By.XPATH,'//*[@id="step-0"]/div[3]/button')  ##Отказываемся от тура новичка
        endtour.click()
        driver.quit()