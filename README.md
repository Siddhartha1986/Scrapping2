
# Flipkart Laptop Data Scraper

## Overview
This repository contains a Python script for scraping laptop data from Flipkart. It navigates through multiple pages of laptop listings, extracting essential details such as titles, prices, and image URLs. The data is then organized into a pandas DataFrame and exported to an Excel file.

## Features
- Extracts laptop titles, prices, and image URLs from Flipkart.
- Navigates through multiple pages to collect a comprehensive dataset.
- Saves the scraped data into an Excel file for easy use and analysis.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Libraries: `requests`, `bs4` (BeautifulSoup), `pandas`

You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 pandas
```

## Usage
1. **Setting the Search Query**: The script is currently set to search for 'laptops'. You can modify the `item_search` variable to scrape data for other products.

2. **Running the Script**: Execute the script in your Python environment. It will automatically scrape data from the first four pages of Flipkart's laptop listings.

3. **Output File**: The script generates an Excel file named `laptops.xlsx`, containing the scraped data.

## Script Details
- The script uses `requests` to send HTTP requests to Flipkart.
- `BeautifulSoup` from `bs4` is employed for parsing HTML content and extracting data.
- `pandas` is used for creating a DataFrame and exporting it to an Excel file.
- The script includes a `sleep` function to pause execution between page requests, reducing the load on Flipkart's servers and mimicking human browsing behavior.

## Note
- Please use this script responsibly and in accordance with Flipkart's terms of service regarding web scraping.
- Ensure that any scraped data is used in compliance with relevant laws and regulations.

## Contributing
Feel free to fork this repository and contribute to its improvement. Whether it's refining the scraping logic, enhancing the data analysis, or fixing bugs, your contributions are welcome!

## License
This script is released under the MIT License.



