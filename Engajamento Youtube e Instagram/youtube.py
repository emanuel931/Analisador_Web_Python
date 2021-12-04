from func import *
from selenium.webdriver.chrome.options import Options as op
from selenium import webdriver as wb

options = op()
options.add_argument('--headless')
options.add_argument('window-size=1280,800')
navegador = wb.Chrome(options=options)

canal = str(input('Digite o Link de um Canal do Youtube: '))
navegador.get(canal)
os_links  = navegador.find_elements_by_tag_name('a')
links = []
for l in os_links:
    href = l.get_attribute('href')
    if href != None:
        if (href.startswith('https://www.youtube.com/watch?v=')):
                    links.append(href)



