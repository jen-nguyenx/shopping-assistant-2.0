import requests
from bs4 import BeautifulSoup
from user_agents import get_random_headers
import logging
import constants as c
from typing import List

logger = logging.getLogger()


def price_scraper(url) -> List[int]:
    try:
        headers = get_random_headers()

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get discounted price
        discounted_price_element = soup.find(
            "span",
            id=c.SPAN_ID.get("discounted"),
        )

        if not discounted_price_element:
            discounted_price_element = soup.select_one(c.SPAN_CLASS("discounted"))

        if not discounted_price_element:
            logger.error("No discounted price found!")
            discounted = None
        else:
            discounted = discounted_price_element.text.strip().replace("$", "")

        # Get full price
        full_price_element = soup.find("span", id=c.SPAN_ID.get("full"))

        if not full_price_element:
            logger.error("No full price found")
            full = None
        else:
            full = full_price_element.text.strip().replace("Don't Pay RRP: $", "")

        return discounted, full

    except Exception as e:
        logging.error(f"Unexpected error occurred {e}")
        return None, None


url = "https://www.chemistwarehouse.com.au/buy/110910/nature-s-way-complete-daily-multivitamin-200-tablets"
a, b = price_scraper(url)
print(a)
print(b)
