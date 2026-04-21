# from logging import exception
import csv
import requests
from bs4 import BeautifulSoup

product_details = []

url = "https://www.jumia.com.eg/catalog/?q=smart+watches"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

products_list = soup.find_all("article", {'class': 'prd'})

for i in range(len(products_list)):
    try:
        products_name = products_list[i].find('h3', {'class': 'name'}).text
    except:
        products_name = "no names found!!"

    try:
        products_price = products_list[i].find('div', {'class': 'prc'}).text
    except:
        products_price = "no prices found!!"

    try:
        products_rate = products_list[i].find('div', {'class': '_s'}).text
    except:
        products_rate = "no rates found!!"

    try:
        products_discount = products_list[i].find('div', {'class': '_sm'}).text
    except:
        products_discount = "no discount found!!"

    product_link = f"https://www.jumia.com.eg{products_list[i].find('a', {'class': 'core'}).get('href')}"

    product_details.append({
        'website': 'jumia',
        'product price ': products_price,
        'discount ': products_discount,
        'product rate ': products_rate,
        'product name ': products_name,
        'product link ': product_link
    })


with open('jumia_products.csv', 'w', newline='', encoding='utf-8-sig') as file:
    fieldnames = [
        'website',
        'product price ',
        'discount ',
        'product rate ',
        'product name ',
        'product link '
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(product_details)

print("CSV file created successfully!")