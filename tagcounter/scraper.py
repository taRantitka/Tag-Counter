import datetime
import requests
import logging
from tld import get_fld
from bs4 import BeautifulSoup
from collections import Counter
from .data_access import DataAccess
from .synonym_helper import SynonymHelper


class Scraper:

    @staticmethod
    def scrape(url):
        synonym = SynonymHelper().read(url)
        if synonym is not None:
            url = f"https://{synonym}"

        logging.info(f"{url} is scraping...")

        page = requests.get(url)
        tags = BeautifulSoup(page.content, "html.parser").find_all()
        report = list(Counter(list(map(lambda t: t.name, tags))).items())

        logging.info(f"{url} has been scraped.")

        site_name = get_fld(url, fix_protocol=True)

        DataAccess().insert((site_name, url, datetime.datetime.now(), report))

        return report
