import time
import schedule
import requests
from bs4 import BeautifulSoup
from datetime import datetime

DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
current_datetime = datetime.now()

def telegram_bot_sendtext(bot_message):
    bot_token = '1735011861:AAE7QTdbPfuG2AF-EZtYIszqc17hdNFtUHI'
    bot_chatID = '833927933'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    full_page = requests.get(DOLLAR_RUB, headers=HEADERS)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    curr = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    res = curr[0].text
    my_message = "Сейчас курс: 1 доллар = {}".format(res)
    telegram_bot_sendtext(my_message)

if current_datetime.weekday() not in (5, 6):
    schedule.every().day.at("15:15").do(report)


while True:
    schedule.run_pending()
    time.sleep(1)