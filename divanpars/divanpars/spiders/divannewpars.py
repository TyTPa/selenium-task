import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svet = response.css('div._Ud0k')
        parsed_data = []
        for sve in svet:
            item = {
                'name': sve.css('div.lsooF span::text').get(),
                'price': sve.css('div.pY3d2 span::text').get(),
                'url': sve.css('a').attrib['href']
            }
            parsed_data.append(item)

# Прописываем открытие нового файла, задаём ему название и форматирование
# 'w' означает режим доступа, мы разрешаем вносить данные в таблицу
        with open("svet_2.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
            writer = csv.writer(file)
    # Создаём первый ряд
            writer.writerow(['Название', 'Цена', 'ссылка на осветительный прибор'])

    # Прописываем использование списка как источника для рядов таблицы
            for data in parsed_data:
                writer.writerow([data['name'], data['price'], data['url']])