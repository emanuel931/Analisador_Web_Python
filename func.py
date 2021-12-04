from selenium import webdriver as wb#Abre os Links
from bs4 import BeautifulSoup as bf #Para Pegar os Preços
from selenium.webdriver.chrome.options import Options
import smtplib
import email.message

def Abrir_Site(navegador, link):
    navegador.get(f'{link}') #Abri o Site
    
    

def Pegar_Info(navegador, onde, param1, param2):
    site = bf(navegador.page_source, 'html.parser') #Abri o HTML
    info = site.find(f'{onde}', attrs={f'{param1}': f'{param2}'}) #Preucura a Informação
    return info


def ee(m1,entregador, recebedor, senha,m2='', m3='', m4='', m5='',ass='Email Automático'):
    corpo_email = f"""
    <p>{m1}</p>
    <p>{m2}</p>
    <p>{m3}</p>
    <p>{m4}</p>
    <p>{m5}</p>

    """
    msg = email.message.Message()
    msg['Subject'] = ass
    msg['From'] = entregador
    msg['To'] = recebedor
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))    