import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = [h1.get_text() for h1 in soup.find_all("h1")]
print("Scraped titles:", titles)
