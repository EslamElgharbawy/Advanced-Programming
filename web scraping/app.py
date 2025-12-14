import requests
from bs4 import BeautifulSoup

url = "https://scrapethissite.com/pages/simple/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

countries = soup.select(".country") 

print("FOUND:", len(countries))

for c in countries:
    name = c.select_one(".country-name").get_text(strip=True)
    capital = c.select_one(".country-capital").get_text(strip=True)
    population = c.select_one(".country-population").get_text(strip=True)
    area = c.select_one(".country-area").get_text(strip=True)

    print(f"{name} | Capital: {capital} | Pop: {population} | Area: {area}")
