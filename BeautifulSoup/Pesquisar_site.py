from selenium import webdriver
from bs4 import BeautifulSoup as bs

class Page:
    def __init__(self, driver):
        """ Por Padrão, ele utiliza o Firefox, mas você poderia mudar de boa ;)"""
        self.driver = driver


Pesquisar = webdriver.Firefox()

Pesquisar.get('http://www.google.com')

print(Pesquisar.page_source)

pagina = bs(Pesquisar,'')