import pandas as pd
import requests

# Send an HTTP POST request to the server
url = 'https://api.mydukaan.io/api/advanced-search/102128463/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Accept': 'application/json, text/plain, /',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'x-requested-with': 'x1rI-1672560044638',
    'Origin': 'https://croptr.in',
    'Connection': 'keep-alive',
    'Referer': 'https://croptr.in/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers'
}
data = {
    "sku_attrs": {},
    "product_attrs": {},
    "sort_by": "bestsellers",
    "category_ids": [11917812],
    "page_size": 18,
    "offset": 0,
    "show_out_of_stock_products": False
}
response = requests.post(url, headers=headers, json=data)

# Save the data in an Excel file
data = response.json()
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
print("task done")
