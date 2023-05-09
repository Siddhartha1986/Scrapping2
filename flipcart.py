import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep


titles = []
prices = []
images = []

for i in range(1,5):
    item_search = "laptops"
    page_number = i
    
    url = f"https://www.flipkart.com/search?q={item_search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_number}"

    response = requests.get(url)
    htmlcontent = response.content
    soup = BeautifulSoup(htmlcontent,'html.parser')

    

    print(f"scrapping data from {i} page of www.flipcart.com for {item_search}")

    for d in soup.find_all('div', attrs = {'class':'_2kHMtA'}):
        title = d.find('div',attrs = {'class':'_4rR01T'} )
        
        price = d.find('div',attrs = {'class':'_30jeq3 _1_WHN1'}) 
        
        image = d.find('img', attrs = {'class':'_396cs4'})
        
        
        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get( 'src' ))
      
    
    print(f"prices from {i} pages are: \n {prices}")
    sleep(1.5)

data = {"TTILES":titles,
        "PRICES":prices,
        "IMAGES":images}

df = pd.DataFrame(data)

print(df)


df.to_excel('laptops.xlsx')