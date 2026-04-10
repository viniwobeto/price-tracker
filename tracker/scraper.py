import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

def search_products(query):
    r = requests.get(f'https://serpapi.com/search.json?engine=google_shopping&q={query}&gl=br&hl=pt&api_key={api_key}')
    data = r.json()
    
    products = []
    for item in data['shopping_results']:
        products.append({
            'title': item['title'],
            'price': item.get('extracted_price'),
            'store': item.get('source'),
            'link': item.get('product_link')
        })
    
    return products

print(search_products('teclado mecanico redragon'))