from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

# Укажите путь к вашему драйверу (например, chromedriver.exe)
driver_path = 'C:\\Users\\Lenovo\\.cache\\selenium\\chromedriver\\win64\\134.0.6998.88\\chromedriver.exe'

# Настройки для Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')  # Если хотите запускать без GUI
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Запуск браузера
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Откройте сайт
driver.get('https://rp5.ru/Архив_погоды_в_Санкт-Петербург')

try:
    # Ждем, пока элемент станет доступным для взаимодействия
    element = driver.find_element(By.XPATH, '//div[@class="inner" and .//div[text()="Выбрать в файл GZ (архив)"]]')

    # Ждем, пока кнопка "Скачать файл" станет доступной
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Скачать файл'))
    )
    download_button.click()

    # Подождите некоторое время, чтобы файл успел скачаться
    time.sleep(10)

finally:
    # Закрыть браузер
    driver.quit()