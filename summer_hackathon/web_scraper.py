import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://999.md/ro/87431652'
# Send a request to the URL
response = requests.get(url)
response.raise_for_status()  # Ensure the request was successful

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
# Find elements by their class name
articles = soup.find_all('div', class_='adPage__content__features__col grid_7 suffix_1')
# Print out each article's details
for article in articles:
    print(article.text)
