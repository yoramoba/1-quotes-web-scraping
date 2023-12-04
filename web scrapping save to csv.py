import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

def scrape_quotes():
    # Send a GET request to the website
    url = 'https://quotes.toscrape.com/page/'
    page_number = 1
    
    while True:
        response = requests.get(url + str(page_number))
        
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes = soup.find_all('div', class_='quote')
        
        with open('quotes.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Quote', 'Author']
            writer = csv.writer(csvfile)
            for quote in quotes:
                writer.writerow([quote.find('span', class_='text').text, quote.find('small', class_='author').text])
        
        
        next_chevron = soup.find('li', class_='next')
        
        if next_chevron:
            page_number += 1
        else:
            break
    
# Call the function to scrape quotes
scrape_quotes()
