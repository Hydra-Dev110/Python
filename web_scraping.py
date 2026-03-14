import requests
from bs4 import BeautifulSoup

# Set URL and headers
url = "https://www.google.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Make the request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all <a> tags and extract href
links = []
for tag in soup.find_all('a', href=True):
    links.append(tag['href'])

# Print all extracted links
for link in links:
    print(link)

