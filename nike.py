import requests
from bs4 import BeautifulSoup as bs
import re

# Define the target url
url = "https://www.nike.com/ca/w/mens-shoes-nik1zy7ok"

# Send a GET request to the URL
response = requests.get(url)

# response.raise_for_status()
status = response.status_code
if status >= 300:
    print(f"Error: {status}")
    exit()

# Parse the HTML content of the page
soup = bs(response.content, 'html.parser')

# Extract product names and prices
products = []

regex = re.compile(r"\d+\.*\d*")
for product in soup.find_all("div", class_="product-card"):
    result = {
        "name": "",
        "price": 0,
        "error": ""
    }
    product_name = product.find("div", class_="product-card__title")
    product_price = product.find("div", class_="product-price")

    if product_name:
        result["name"] = product_name.text.strip()
    else:
        result["error"] = "Name not found"

    if product_price:
        striped_price = regex.search(product_price.text.strip())
        result["price"] = float(striped_price.group())
    else:
        result["error"] = "Price not found"
    products.append(result)

print(products)