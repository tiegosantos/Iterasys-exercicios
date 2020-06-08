from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import unittest, time, re

import json
import csv
import lxml.html as parser
import requests
import csv

'''
1) Crie uma consulta que retorne uma lista com pelo menos 3 carros usados da mesma marca modelo,
os demais critérios da consulta são a sua escolha.

Res: Usei o plugin katalon recorder - selenium para gravar a tela e gerar o código,
em seguida exportando o mesmo para python.
Tentei usar técnica de Web Scraping usando Python e Selenium.

-- Imaginei em criar a consulta automatica (1) e em seguida criar o
arquivo de dados (3)para em seguida realizar as validações(2) e (4)

'''
#Acessando o site de forma automatica e pesquisando os veículos
driver = webdriver.Chrome()
driver.get("https://www.icarros.com.br/principal/index.jsp")
driver.find_element_by_xpath("//button[@type='button']").click()
driver.find_element_by_link_text("Volkswagen").click()
Select(driver.find_element_by_id("sltMake")).select_by_visible_text("Volkswagen")
driver.find_element_by_link_text("Fox").click()
Select(driver.find_element_by_id("sltModel")).select_by_visible_text("Fox")
driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
driver.find_element_by_link_text("De 2019").click()
Select(driver.find_element_by_id("sltYearMin")).select_by_visible_text("De 2019")
driver.find_element_by_xpath("//form[@id='buscaForm']/div[3]/div[2]/div/div/div/div/button/span").click()
driver.find_element_by_link_text(u"Até 2020").click()
Select(driver.find_element_by_id("sltYearMax")).select_by_visible_text(u"Até 2020")
driver.find_element_by_xpath("//section/div").click()
driver.find_element_by_xpath("//form[@id='buscaForm']/div[4]/div[2]/button").click()
lista =  driver.find_element_by_xpath('/*[@id="anunciosForm"]/ul')

'''
3)Obtendo os dados
O script deve ler a lista de resultados e criar um arquivo de dados contendo 
marca,modelo,ano,km,cor,câmbio e valor à vista de cada veiculo
retornado (apenas da primeira página de retorno)

Res: Tentei utilizar técnica  Xpath para pegar os dados das tags
Instalei plugins Xpath Helper para o chrome para validar os Xpath 
'''


marca = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/a/h2/span/span')
marcatext = marca.text

modelo = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/a/h2/text()')
modelotext = modelo.text

ano = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/div[2]/div[1]/a/ul/li[1]/p')
anotext = ano.text

km = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[2]/div/div[2]/div[1]/a/ul/li[2]')
kmtext = km.text

cor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[2]/div/div[2]/div[1]/a/ul/li[2]')
cortext = cor.text

cambio = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/div[2]/div[1]/a/ul/li[4]/p')
cambiotext = cambio.text

valor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[3]/div[3]/div[2]/div[4]/form/ul/li[1]/div/a/h3/text()')
valortext = valor.text

print("Marca: " + marcatext)
print("Modelo: " + modelotext)
print("Ano: " + anotext)
print("km: " + kmtext)
print("Cor: " + cortext)
print("Cambio: " + cambiotext)
print("Valor: " + valortext)
print('-----------------------------')

dados = marcatext +';'+ modelotext +';' + anotext + ';' + kmtext + ';' + cambiotext + ';' + valortext
self.salvaDados(dados)


def salvaDados(self, dados):
    arquivo = open('C:/Users/galodoido/Desktop/testes - ' + '.txt', 'a')
    arquivo.write(dados + '\n')
    arquivo.close()


