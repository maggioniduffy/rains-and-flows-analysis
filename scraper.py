from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import ChromeOptions

PATH = '/usr/bin/chromedriver'
options = ChromeOptions()
options.add_argument("--headless=new")

browser = webdriver.Chrome(options=options)

urls = ['http://www.aic.gov.ar/sitio/embalses','https://www.accuweather.com/en/ar/national/weather-radar']

browser.get(urls[0])

btn = browser.find_element('#mapa > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(2)')
btn.click()

q_in = browser.find_element('#mapa > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(4) > div > div > div > div.gm-style-iw.gm-style-iw-c > div.gm-style-iw-d > div > div > div.MenDatos > table > tbody > tr:nth-child(6) > td:nth-child(2)')
q_out = browser.find_element('#mapa > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(4) > div > div > div > div.gm-style-iw.gm-style-iw-c > div.gm-style-iw-d > div > div > div.MenDatos > table > tbody > tr:nth-child(9) > td:nth-child(2)')

browser.close()

browser.get(urls[1])

browser.quit()

# #mapa > div > div.gm-style > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(2)