from selenium import webdriver
import random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time

chromedriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome()
service = Service(executable_path=chromedriver_path)


try:
    # Открываем страницу Википедии
    driver.get("https://www.wikipedia.org/")
    time.sleep(2)

    # Находим окно поиска и вводим запрос
    search_box = driver.find_element(By.ID, "searchInput")
    query = input("Введите, что хотите найти в Википедии\n")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    i = 0
    while i < 3:
        choice_m = input(
            "Нажмите\n 1 если хотите листать параграфы\n 2 перейти на одну из связанных страниц \n 3 выйти из программы \n")

        if choice_m == '1':
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input("Нажмите Enter для продолжения...")
                i += 1
                if i >= 3:
                    break

        elif choice_m == '2':
            # Находим первую видимую ссылку в содержимом статьи
            content = driver.find_element(By.ID, "mw-content-text")
            links = content.find_elements(By.TAG_NAME, 'a')
            for link in links:
                if link.is_displayed():
                    link.click()
                    break
                time.sleep(2)
                i += 1


        elif choice_m == '3':
            break

    # Печатаем текущий URL
    print("Current URL:", driver.current_url)

finally:
    # Закрываем браузер
    driver.quit()