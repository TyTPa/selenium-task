#Код, написанный с использованием  Selenium.
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(10)

svet = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for sve in svet:
    try:
        title_element = sve.find_element(By.CSS_SELECTOR,  'div.lsooF span')
        title = title_element.text
        link = sve.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        price = sve.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("svet2.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка на осветительный прибор'])
    writer.writerows(parsed_data)