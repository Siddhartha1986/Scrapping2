import requests                  # For sending HTTP requests to the website
from bs4 import BeautifulSoup    # For parsing HTML content
import pandas as pd              # For data manipulation and analysis
from time import sleep           # For pausing the execution between page requests

# Lists to store the extracted data
titles = []
prices = []
images = []

# Loop to scrape multiple pages
for i in range(1, 5):  # Scraping the first four pages
    item_search = "laptops"  # Search query
    page_number = i  # Current page number
    
    # Constructing the URL for each page
    url = f"https://www.flipkart.com/search?q={item_search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page_number}"

    # Sending a GET request to the URL
    response = requests.get(url)
    htmlcontent = response.content  # Getting the content of the page
    soup = BeautifulSoup(htmlcontent, 'html.parser')  # Parsing the HTML content

    print(f"Scraping data from page {i} of www.flipkart.com for {item_search}")

    # Loop to extract data from each product listing on the page
    for d in soup.find_all('div', attrs={'class': '_2kHMtA'}):  # Finding each product container
        title = d.find('div', attrs={'class': '_4rR01T'})  # Extracting the title
        price = d.find('div', attrs={'class': '_30jeq3 _1_WHN1'})  # Extracting the price
        image = d.find('img', attrs={'class': '_396cs4'})  # Extracting the image URL
        
        # Adding the extracted data to the respective lists
        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get('src'))
      
    print(f"Prices from page {i} are: \n {prices}")
    sleep(1.5)  # Pausing for 1.5 seconds before scraping the next page

# Creating a DataFrame with the extracted data
data = {"TITLES": titles, "PRICES": prices, "IMAGES": images}
df = pd.DataFrame(data)

print(df)  # Printing the DataFrame

df.to_excel('laptops.xlsx')  # Saving the data to an Excel file
