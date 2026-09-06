import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()

except requests.RequestException as error:
    print(f"Request failed: {error}")
    raise SystemExit(1)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.select(".quote")

if not quotes:
    print("No quotes found on the page.")
    raise SystemExit(0)

saved = 0

with open("quotes.txt", "w", encoding="utf-8") as file:
    for quote in quotes:
        text_element = quote.select_one(".text")
        author_element = quote.select_one(".author")

        text = (
            text_element.get_text(strip=True)
            if text_element
            else "[Missing quote]"
        )

        author = (
            author_element.get_text(strip=True)
            if author_element
            else "[Unknown author]"
        )

        line = f"{author}: {text}"
        print(line)
        file.write(line + "\n")
        saved += 1

print(f"\nSaved {saved} quotes to quotes.txt")
