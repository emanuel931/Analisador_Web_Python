# Entrar Nos Sites(Magazine Luiza, Casas Bahia, Amazon e Americanas);
# Pegar Preços;
# E Enviar uma Planilha com Todos os Preços no Gmail e Tambem o Menor Preço

# Modúlos
from selenium import webdriver as wb#Abre os Links
from bs4 import BeautifulSoup as bf #Para Pegar os Preços
from time import sleep
from selenium.webdriver.chrome.options import Options as op
import pandas as pd
from datetime import datetime
from func import *




opt = op()
opt.add_argument('window-size=1280,720')

navegador = wb.Chrome(options=opt) # Para Temos Acesso ao Navegador

# Abrir Amazon e Pegar Preço
link = str('https://www.amazon.com.br/poder-do-hábito-Charles-Duhigg/dp/8539004119/ref=sr_1_5?__mk_pt_BR=ÅMÅŽÕÑ&crid=2UL2CJAS1S4T1&keywords=poder+do+habito&qid=1638388814&sprefix=poder+d%2Caps%2C1427&sr=8-5')
preçoAmazon = Pegar_Info(navegador,  link, 'span', 'id', 'price')

pv = '' 
for l in preçoAmazon:
    if (l.isnumeric()):
        pv = pv +l
    elif l == ',':
        pv = pv + '.'

preçoAmazon = float(pv) #Muda o Preço Para Float
p = preçoAmazon
pn = 'Amazon'
pl = 'https://www.amazon.com.br/poder-do-hábito-Charles-Duhigg/dp/8539004119/ref=sr_1_5?__mk_pt_BR=ÅMÅŽÕÑ&crid=2UL2CJAS1S4T1&keywords=poder+do+habito&qid=1638388814&sprefix=poder+d%2Caps%2C1427&sr=8-5'


# Abrir Casas Bahia e Pegar Preço
link = 'https://www.casasbahia.com.br/livros/AutoajudaRelacionamentos/Autoajuda/poder-do-habito-o-5508320.html?IdSku=5508320'
preçoBahia = Pegar_Info(navegador, link, 'span', 'id', 'product-price')

pv = ''
for l in preçoBahia:
    if (l.isnumeric()):
        pv = pv + l
    elif l == ',': 
        pv = pv + '.'
preçoBahia = float(pv)
if preçoBahia < p:
    p = preçoBahia
    pn = 'Casas Bahia'
    pl = 'https://www.casasbahia.com.br/livros/AutoajudaRelacionamentos/Autoajuda/poder-do-habito-o-5508320.html?IdSku=5508320'

# Abrir Americanas e Pegar Preço
link = str('https://www.americanas.com.br/produto/111949251?chave=acproduct')
preçoAmericanas = Pegar_Info(navegador,  link, 'div', 'class', 'src__BestPrice-sc-1jvw02c-5 cBWOIB priceSales')

pv = ''
for l in preçoAmericanas:
    if (l.isnumeric()):
        pv = pv + l
    if l == ',':
        pv = pv  + '.'
preçoAmericanas= float(pv)
if preçoAmericanas < p:
    p = preçoAmericanas
    pn = 'Americanas'
    pl = 'https://www.americanas.com.br/produto/111949251?chave=acproduct'

ee(f'Menor Preço, {pn}:', 'baitisatae@gmail.com', 'batistaemanuel324@gmail.com', '88900912',m2=f'Preço: {p :.2f}',m3=f'Link = {pl}',ass='Preço do Livro Poder do Hábito')

preços = {'Site de Vendas':['Amazon', 'Casas Bahia', 'Americanas'],
'Preços': [preçoAmazon, preçoBahia, preçoAmericanas]
}

preços_df = pd.DataFrame(preços)
dia = datetime.today().strftime('%d %m %Y')

print(preços_df)

#Salvar No Excel
arq = pd.ExcelWriter(f'Preços do Dia {dia}.xlsx')
preços_df.to_excel(arq, 'Livro', index=False)
arq.save()
