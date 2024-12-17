#!/usr/bin/python3
"""
A crawler to get data from wikipedia.

:Copyright:
    Copyright 2023 A-Insights.  All Rights Reserved.
"""

import logging
import time

# import mariadb


LOGGER_NAME = "wiki_crawler"


class WikiCrawler:
    """
    A crawler that extract data from wikipedia pages then save the data in MariaDB.
    """
    def __init__(
            self
    ):
        """
        Initialise the WikiCrawler.
        """
        self._logger = logging.getLogger(LOGGER_NAME)

        # TODO: Get ENV VAR parameters of mariadb

    @staticmethod
    def get_crawl_list():
        # Sleep for 10 seconds in case the crawler starts too fast while the mariadb is not ready.
        time.sleep(10)
        return [
            'https://en.wikipedia.org/wiki/Winged_Victory_of_Samothrace',
            'https://en.wikipedia.org/wiki/Girl_with_a_Pearl_Earring',
            'https://en.wikipedia.org/wiki/Elden_Ring'
        ]

    def crawl(self, url):
        """
        Main crawling function, get the title, summary, image_url of the wikipedia page.

        :param url: The URL of wikipedia page to crawl
        :return:
        """
        # TODO: Please implement this function
        pass

    def save(self, article):
        """
        Save the wikipedia data to the table 'wiki_articles'

        :return:
        """
        # TODO: Please implement this function
        pass

    def run(self):
        # Setup logging for the script
        logging.basicConfig(level=logging.INFO)
        crawl_list = self.get_crawl_list()

        for url in crawl_list:
            article = self.crawl(url)
            self.save(article)


if __name__ == '__main__':

    crawler = WikiCrawler()
    crawler.run()
