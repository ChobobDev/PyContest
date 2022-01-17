import requests
from bs4 import BeautifulSoup

def requestWithUgerAgent(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.360'}
    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
    return soup
