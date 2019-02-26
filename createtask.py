from selenium import webdriver
import unittest
import time
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
        web = driver.find_element(By.XPATH, '//*[@id="id_web_app_link"]') ##Нажимаем кнопку Web
        web.click()
        web_app = driver.find_element(By.XPATH, '//*[@id="id_new_webapp_link"]') ##Нажимаем  "Add a new web app"
        web_app.click()
        nextbtn = driver.find_element(By.XPATH, '// *[ @ id = "id_create_web_app_wizard"] / div[2] / div / button[2]') ##Нажимаем Next
        nextbtn.click()
        flask = driver.find_element(By.XPATH, '//*[@id="id_create_web_app_wizard_quickstart_choice_step"]/ul/li[3]/button/b') ##Выбираем Flask
        flask.click()
        py37 = driver.find_element(By.XPATH, '//*[@id="id_flask_python_version_step"]/ul/li[5]/button/b') ##Выбираем py 3.7
        py37.click()
        nextbtn2 = driver.find_element(By.XPATH, '//*[@id="id_create_web_app_wizard"]/div[2]/div/button[2]') ##Нажимаем next
        nextbtn2.click()
        time.sleep(15) ##Создание работает не быстро, поэтому лучше подождать немного
        assert driver.find_element(By.XPATH,'//*[@id="id_741852_pythonanywhere_com"]/div[1]/div/h3').text == "Configuration for 741852.pythonanywhere.com": ##Проверяем что все создалось без ошибок
        driver.quit()
