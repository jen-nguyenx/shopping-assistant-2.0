import logging
from typing import List

import undetected_chromedriver as uc
from bs4 import BeautifulSoup

import price_tracker.constants as c
from price_tracker.user_agents import get_random_headers

logger = logging.getLogger()


def price_scraper(url: str, get_name: bool = False) -> List[int | str | None]:
    try:
        options = uc.ChromeOptions()

        # Add arguments to make it the browsing context more human-like
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.headless = False

        driver = uc.Chrome(options=options, use_subprocess=True, version_main=131)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

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
            logger.error("No full price found, no discount applied on the product")
            full = discounted
        else:
            full = full_price_element.text.strip().replace("Don't Pay RRP: $", "")

        # Get product name
        name = None
        if get_name:
            name = extract_product_name(soup)
        driver.quit()
        return discounted, full, name

    except Exception as e:
        logging.error(f"Unexpected error occurred {e}")
        return None, None, None


def extract_product_name(soup: BeautifulSoup) -> str:
    try:
        target_element = soup.find("div", class_="product-name")

        if target_element:
            h1_block = target_element.find("h1")
            if h1_block:
                name = h1_block.text.strip()
            else:
                logging.error("No product name found")
                name = None

    except Exception as e:
        logging.error(f"Unexpected error occurred {e}")
        return None

    return name


def bulk_extract_brand_names(url: str) -> List[str]:
    try:
        options = uc.ChromeOptions()

        # Add arguments to make it the browsing context more human-like
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.headless = False

        driver = uc.Chrome(options=options, use_subprocess=True, version_main=131)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Find category names
        brand_divs = soup.find_all("div", class_="category-results-top-category__name")

        brands = [div.text.strip() for div in brand_divs if div.text.strip()]

        driver.quit()

        return brands

    except Exception as e:
        logging.error(f"Unexpected error occurred {e}")
        return None
