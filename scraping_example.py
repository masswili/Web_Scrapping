import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    # Mengambil konten HTML dari halaman web
    response = requests.get(url)
    if response.status_code == 200:
        # Parsing HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Menemukan elemen yang ingin di-scrape (misalnya, judul artikel)
        titles = soup.find_all('h2', class_='mp-h2')
        data = []
        for title in titles:
            # Menyimpan judul ke dalam list data
            data.append(title.text.strip())
        return data
    else:
        print('Failed to fetch the website:', response.status_code)
        return None

def save_to_csv(data, filename):
    # Menyimpan data ke dalam file CSV
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title'])
        for title in data:
            writer.writerow([title])

if __name__ == '__main__':
    # URL dari website yang ingin di-scrape
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    # Melakukan web scraping
    scraped_data = scrape_website(url)
    if scraped_data:
        # Menyimpan hasil scraping ke dalam file CSV
        save_to_csv(scraped_data, 'scraped_data.csv')
        print('Scraping completed. Data saved to scraped_data.csv')
