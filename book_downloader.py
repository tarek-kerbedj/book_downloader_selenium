from selenium import webdriver
import bs4
import time
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path=input('insert the path to your geckodriver.exe')
book_names=input('choose a name of your book \n').split(',')
#takes a list of books seperated by commas as input
extension=input('choose your extension pdf,epub,txt \n')
#takes only one extension as a parameter (for now)

#browser=webdriver.Firefox(executable_path='C:\\Users\\Oxidiovega\\Desktop\\geckodriver.exe')
browser=webdriver.Firefox(executable_path=driver_path)

browser.get('https://z-lib.org/')

books_button=browser.find_element_by_css_selector('div.col-sm-4:nth-child(1) > a:nth-child(1)')
books_button.click()
#selects the domain based on your location
wait=WebDriverWait(browser,10)
search_element=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchFieldx"]')))
search_element.click()
#wait for the search bar to appear and then click

def extra_options(extension):
		search_options_button=browser.find_element_by_css_selector('#advSearch-control')
		#search_options_button=wait.until(EC.element_to_be_clickable((By.XPATH,"html body.index.startForm table tbody tr td.g-page-content div.container div.row div.col-md-12.itemFullText div#searchFormWithLogo form#searchForm div div#advSearch-wrapper div span#advSearch-control")))
		search_options_button.click()
		time.sleep(0.3)
		#extension_button=wait.until(EC.element_to_be_clickable((By.XPATH,"#wrapExt > div:nth-child(1) > input:nth-child(1)")))
		extension_button=browser.find_element_by_css_selector('#wrapExt > div:nth-child(1) > input:nth-child(1)')
		extension_button.click()
		if extension=='pdf':

			extension_pdf=browser.find_element_by_css_selector('div.multiselect-item-wrap:nth-child(9) > span:nth-child(2)')
			extension_pdf.click()

		elif(extension=='epub'):
			extension_epub=browser.find_element_by_css_selector('div.multiselect-item-wrap:nth-child(5) > span:nth-child(2)')
			extension_epub.click()
		elif(extension=='txt'):
			extension_txt=browser.find_element_by_css_selector('div.multiselect-item-wrap:nth-child(11) > span:nth-child(2)')
			extension_text.click()
		else:
			return None
i=0
for book in book_names:
	i=i+1
	if (i>1):

		home=browser.find_element_by_css_selector('#colorBoxes > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)')
		home.click()
		extra_options(extension)
		searchfield=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchFieldx"]')))

		searchfield.click()
		
		
		searchfield.send_keys(book)
		searchfield.submit()
		result=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a")))
		result.click()
		


	else:
		extra_options(extension)		
		search_element.send_keys(book)
		search_element.submit()
		result=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a")))	
		if result is not None:
			result.click()
			download_button=browser.find_element_by_css_selector('a.btn-primary')
			download_button.click()
