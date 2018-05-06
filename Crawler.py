from bs4 import BeautifulSoup
import lxml
import requests

answers = requests.get('https://no1s.biz/')
bs = BeautifulSoup(answers.text,'lxml')
urls = bs.findAll('a')
for url in urls:
    print('{} {}'.format(url.get('href'), bs.a.string))
