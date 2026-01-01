import requests
from bs4 import BeautifulSoup as bs
import re
import csv
import plotly.express as px
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac
# Define the target url
url = "https://www.nike.com/ca/w/mens-shoes-nik1zy7ok"

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
total_product = driver.find_element(By.CLASS_NAME, "wall-header__item_count").text
total_product = int(re.search(r"\d+", total_product).group())
chain = ac(driver)

while True:
    try:
        load_more = driver.find_elements(By.CLASS_NAME, "product-card")[-1]
        if load_more.get_attribute("data-product-position") == total_product:
            break
        # bottom_elem = driver.find_element(By.ID, "app-root")
        chain.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)
    except IndexError:
        break

# # Send a GET request to the URL
# response = requests.get(url)

# # response.raise_for_status()
# status = response.status_code
# if status >= 300:
#     print(f"Error: {status}")
#     exit()


# Parse the HTML content of the page
soup = bs(driver.page_source, 'html.parser')

# Extract product names and prices
products = []

regex = re.compile(r"\d+\.*\d*")
for product in soup.find_all("div", class_="product-card"):
    result = {
        "name": "",
        "price": 0
    }
    product_name = product.find("div", class_="product-card__title")
    product_price = product.find("div", class_="product-price")

    if product_name:
        result["name"] = product_name.text.strip()


    if product_price:
        striped_price = regex.search(product_price.text.strip())
        result["price"] = float(striped_price.group())

    products.append(result)

# print(products)

# write to a csv file
csv_path = "python_tutorial/scrawler/nike_mens_shoes.csv"

with open(csv_path, mode="w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

# plot the product to a histogram
prices = [product["price"] / 1.34 for product in products]


fig = px.histogram(x=prices, nbins=20, title="Nike men's shoes")
fig.show()