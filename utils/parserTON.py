import requests
from bs4 import BeautifulSoup


class Currency:
    @staticmethod
    async def get_currency_price():
        # Парсим всю страницу
        url = "https://www.binance.com/ru/price/toncoin"
        full_page = requests.get(url)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("div", class_="css-12ujz79")
        num = convert[0].text.replace("$ ", "")
        return int(round(float(num)))
