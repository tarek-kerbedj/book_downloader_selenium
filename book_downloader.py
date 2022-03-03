from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# takes a list of books seperated by commas as input

book_names=input('choose a name of your book \n').split(',')

# list of supported extension and their css id 

extension_dictionary={'pdf':9,'epub':5,'txt':11}

# takes only one extension as a parameter (for now)

while True:  
    extension=input('choose your extension pdf,epub,txt \n').strip().lower()
    if extension not in extension_dictionary.keys():
        pass
    else:
        break

# setting up the browser

s=Service('geckodriver.exe')
browser = webdriver.Firefox(service=s)

# this opens up the browser and redirects to this website
browser.get('https://z-lib.org/')

# selects the domain based on your location
books_button = browser.find_element(by=By.CSS_SELECTOR, value='div.col-sm-4:nth-child(1) > a:nth-child(1)')
books_button.click()

# creating a waiting object that halts the program after 10 seconds of waiting
wait = WebDriverWait(browser,10)


def extra_options(extension):
    
    # click on the advanced search button
    search_options_button = browser.find_element(by=By.CSS_SELECTOR, value='#advSearch-control')
    
    search_options_button.click()
    
    # wait until the extension button appears and then click on it
    extension_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#wrapExt > div:nth-child(1) > input:nth-child(1)')))
    extension_button.click()
    # select the extension from the list and click on it
    extension = browser.find_element(by=By.CSS_SELECTOR, value=f'div.multiselect-item-wrap:nth-child({extension_dictionary[extension]})> span:nth-child(2)')
    extension.click()
    
def download_book(book):
    # type the book name and submit it 
    search_element.send_keys(book)
    search_element.submit()
    # wait for the results 
    result = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a")))	
    if result is not None:
        # click on the result
        result.click()
        # find the download button and press it
        download_button = browser.find_element(by=By.CSS_SELECTOR, value='a.btn-primary')
        download_button.click()
             
for book in book_names:
    # click in the chosen extension
    extra_options(extension)
    search_element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="searchFieldx"]')))
    search_element.click()
    # type the book name and submit it
    download_book(book)

    # return home for another query
    home=browser.find_element(by=By.CSS_SELECTOR,value='#colorBoxes > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)')
    home.click()
   
