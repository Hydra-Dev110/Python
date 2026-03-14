
import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract page title
    title = soup.find("title").text
    print("Page Title:", title)

    # Extract all links
    links = soup.find_all("a")
    print("\nLinks found on the page:")
    for link in links:
        print(link.get("href"))
else:
    print("Failed to retrieve the webpage")
