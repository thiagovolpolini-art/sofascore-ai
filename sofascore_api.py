import cloudscraper

scraper = cloudscraper.create_scraper()

url = "https://www.sofascore.com/api/v1/unique-tournament/17/season/76986/player-of-the-season-race"

response = scraper.get(url)

print("STATUS:", response.status_code)

print(response.json())