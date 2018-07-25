# Coder: Kousha Zanjani
# License: Apache License 2.0
from smtplib import SMTP
import requests
import threading


def send_mail(message):
    receiver_emails_list = ['receiver1@gmail.com', 'receiver2@gmail.com']
    sender_email = 'yourEmail@gmail.com'
    server = SMTP('smtp.gmail.com', 25)
    server.starttls()
    server.login(sender_email, 'yourPassword')
    server.sendmail(sender_email, receiver_emails_list,
                    'Current Bitcoin is %s' % message)
    server.quit()


def main():
    threading.Timer(120.0, main).start()
    url_api = 'https://api.coinbase.com/v2/prices/buy?currency=USD'
    response = requests.get(url_api)
    bitcoin_price = response.json()['data']['amount']
    intBitcoin_price = float(bitcoin_price)
    if intBitcoin_price < 5000:
        send_mail(bitcoin_price)
    print('Working ...')


if __name__ == '__main__':
    main()
