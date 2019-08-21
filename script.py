import requests
from bs4 import BeautifulSoup
import smtplib

def parse_amazon(url, user_price):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    URL = url
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'html5lib')

    price = soup.find('span', attrs = {'id': 'priceblock_ourprice'}).get_text()
    price_updated = int(price[1:3])
    print(price_updated)
    if price_updated < user_price:
        send_email()



def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('matt.mcneive@gmail.com', 'fuczqthhokialmwl')
    subject = 'Price Drop'
    body = 'Amazon price fell    https://www.amazon.com/dp/B01G6IOEF6/ref=twister_B07GR6XHJ8?_encoding=UTF8&psc=1'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('matt.mcneive@gmail.com', 'mmcneive@luc.edu', msg)
    print('Email Sent')
    server.quit()


parse_amazon('https://www.amazon.com/dp/B01G6IOEF6/ref=twister_B07GR6XHJ8?_encoding=UTF8&psc=1', 25)
