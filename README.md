# BeautifulSoup Quotes Scraper

A beginner Python web scraper built with Requests and BeautifulSoup.

## Features

- Sends an HTTP request to a public website
- Parses HTML using BeautifulSoup
- Extracts quotes and authors
- Saves scraped data to `quotes.txt`

## Requirements

- Python 3.12+
- requests
- beautifulsoup4

## Run

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install requests beautifulsoup4
python scraper.py
