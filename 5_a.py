from urllib.parse import urljoin
import bs4
import pandas as pd
import requests

url = 'https://books.toscrape.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


all_books_data = []

while url:
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        break

    soup = bs4.BeautifulSoup(response.content, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text

       
        all_books_data.append({'Book Title': title, 'Price': price})

    next_li = soup.find('li', class_='next')

    if next_li:
        next_page_rel = next_li.a['href']
        url = urljoin(url, next_page_rel)
    else:
        url = None


df = pd.DataFrame(all_books_data)
df.to_excel('all_books.xlsx', index=False)

print("Process completed! Data exported to all_books.xlsx 🟢")