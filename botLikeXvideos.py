import os
try:
	from selenium import webdriver
except Exception:
	os.system('pip install selenium')

url = str(input('Qual O Video? (URL) -> '))
coment = str(input('copie o XPATH Do Like No comentario. -> '))
qntd = int(input('Quantos Like Deseja Receber? -> '))

for x in range(qntd):
	browser = webdriver.Firefox()
	browser.get(url)
	browser.maximize_window()
	browser.find_element_by_xpath(coment).click()
	browser.quit()