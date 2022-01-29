import requests
from stem import Signal
from stem.control import Controller

with Controller.from_port(port = 9051) as c:
    c.authenticate()
    c.signal(Signal.NEWNYM)

url = 'https://v4.ident.me'
curr_ip = ''
new_ip = ''

proxies = {
    'http':  'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def check_ip(url, prox=None):
    if prox: return requests.get(url, proxies=prox).text
    else: return requests.get(url).text

def get_ip(prox):
    return requests.get('https://api.ipify.org', proxies=proxies).text

print(check_ip(url, proxies))
print(get_ip(proxies))
