import requests
from dotenv import load_dotenv
import os
from urllib.parse import quote

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

def search_products(query):
    r = requests.get(f'https://serpapi.com/search.json?engine=google_shopping&q={quote(query)}&gl=br&hl=pt&api_key={api_key}')
    data = r.json()

    products = []
    for item in data['shopping_results']:
      products.append({
        'title': item.get('title', 'N/A'),
        'price': str(item.get('extracted_price', 'N/A')),
        'store': item.get('source', 'N/A'),
        'link': item.get('product_link', 'N/A')
    })

    return products


