from celery import shared_task
from price_tracker.price_scraper import price_scraper

@shared_task
def scrape_all_prices():
    url = "https://www.chemistwarehouse.com.au/buy/69163/swisse-ultiboost-magnesium-200-tablets"
    price_scraper(url)
    print("HELLO")