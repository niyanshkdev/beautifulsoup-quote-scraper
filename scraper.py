import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

with open("quotes.txt", "w", encoding="utf-8") as file:
    for quote in soup.select(".quote"):
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)

        line = f"{author}: {text}"
        print(line)
        file.write(line + "\n")
