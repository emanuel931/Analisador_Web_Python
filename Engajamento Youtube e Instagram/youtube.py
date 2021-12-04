from func import *
from selenium.webdriver.chrome.options import Options as op
from selenium import webdriver as wb

options = op()
options.add_argument('--headless')
options.add_argument('window-size=1280,800')
navegador = wb.Chrome(options=options)
