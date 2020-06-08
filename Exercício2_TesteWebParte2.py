from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import csv
import requests



driver = webdriver.Chrome()
driver.get("https://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&anunciosNovos=1&anunciosUsados=1&marca1=36&modelo1=478&anomodeloinicial=2019&anomodelofinal=2020&precominimo=0&precomaximo=0&cidadeaberto=&escopo=2&locationSop=est_MG.1_-cid_2754.1_-esc_2.1_-rai_50.1_")

modelo = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/a/h2/text()')
modelotext = modelo.text

valor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/a/h3/text()')
valortext = valor.text

'''
2) Valide o modelo e o valor à vista do primeiro e do segundo carro da 
lista produzida pela consulta.

'''
arquivo = open('dados.csv')
dados = csv.DictReader(arquivo)
for carros in dados:
    if (modelo != ' ' and valor != ' '):
        print ('valores corretos')
    else: 
        print ('valores incorretos')
   
