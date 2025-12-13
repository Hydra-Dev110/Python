import requests
from bs4 import BeautifulSoup


def file_operations():
    data = [
        "DevOps involves collaboration",
        "Automation improves efficiency",
        "Python is widely used in DevOps"
    ]

    # Write data to file
    with open("sample.txt", "w") as file:
        for line in data:
            file.write(line + "\n")

    print("File written successfully.")

    # Read and process file
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)

    print("Number of lines:", line_count)
    print("Number of words:", word_count)



def web_scraper():
    url = "https://example.com"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract page title
        title = soup.find("title").text
        print("\nWeb Scraping Output")
        print("Page Title:", title)

        # Extract all links
        print("Links found:")
        for link in soup.find_all("a"):
            print(link.get("href"))
    else:
        print("Failed to retrieve webpage")


# -----------------------------
# MAIN EXECUTION
# -----------------------------

if __name__ == "__main__":
    print("Running File Operations...")
    file_operations()

    print("\nRunning Web Scraper...")
    web_scraper()
