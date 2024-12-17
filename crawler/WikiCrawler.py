#!/usr/bin/python3
"""
A crawler to get data from wikipedia.

:Copyright:
    Copyright 2023 A-Insights.  All Rights Reserved.
"""

import mariadb  
import logging  
import os  
import time  
import requests  
from bs4 import BeautifulSoup  


LOGGER_NAME = "wiki_crawler"

class WikiCrawler:
    """
    A crawler that extract data from wikipedia pages then save the data in MariaDB.
    """
    def __init__(self):
        """
        Initialise the WikiCrawler.
        """
        self._logger = logging.getLogger(LOGGER_NAME)
        
        # Set up logging configuration 
        logging.basicConfig(level=logging.INFO) 

        # Get ENV VAR parameters for MariaDB using os 
        self.db_host = os.getenv('MARIADB_HOST', 'mariadb') 
        self.db_user = os.getenv('MARIADB_USER', 'crawler') 
        self.db_password = os.getenv('MARIADB_PASSWORD', 'a-insights') 
        self.db_name = os.getenv('MARIADB_DATABASE', 'crawler_dev') 

        # Attempt to connect to MariaDB 
        self._logger.info(f"Connecting to MariaDB at {self.db_host}...") 
        try: 
            self.connection = mariadb.connect( 
                host=self.db_host, 
                user=self.db_user, 
                password=self.db_password, 
                database=self.db_name) 
            self.cursor = self.connection.cursor() 
            self._logger.info("Database connection established.") 
        except mariadb.Error as e: 
            self._logger.error(f"Error connecting to MariaDB: {e}") 
            raise 

    @staticmethod
    def get_crawl_list() -> list:
        # Sleep for 10 seconds in case the crawler starts too fast while the mariadb is not ready.
        time.sleep(10)
        return [
            'https://en.wikipedia.org/wiki/Winged_Victory_of_Samothrace',
            'https://en.wikipedia.org/wiki/Girl_with_a_Pearl_Earring',
            'https://en.wikipedia.org/wiki/Elden_Ring'
        ]

    def crawl(self, url: str):
        """
        Main crawling function, gets the title, summary, image_url of the wikipedia page.
        :param url: The URL of wikipedia page to crawl
        :return: Dictionary with title, summary, and image_url or None if error occurs.
        """

        self._logger.info(f"Starting to crawl: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the title
            title = soup.find('h1', id='firstHeading').get_text(strip=True)

            # Extract the summary (first 150 words of the main content)
            paragraphs = soup.find_all('p', limit=7)  # Fetch first few paragraphs
            summary = ""
            for p in paragraphs:
                summary += p.get_text(strip=True) + " "
                if len(summary.split()) > 150:
                    summary = " ".join(summary.split()[:150])  # Limit to 150 words
                    break

            # Extract the main image URL (if available)
            image_tag = soup.find('img')
            image_url = f"https:{image_tag['src']}" if image_tag else None

            self._logger.info(f"Crawled data - Title: {title}, Summary Length: {len(summary)}, Image URL: {image_url}")
            return {'title': title, 'summary': summary, 'image_url': image_url}
        except Exception as e:
            self._logger.error(f"Error while crawling {url}: {e}")
            return None


    def save(self, article: dict):
        """
        Save the wikipedia data to the table 'wiki_articles' table in MariaDB.
        :param article: A dictionary containing 'title', 'summary', and 'image_url'.
        :return: True or False
        """
        if not article:
            self._logger.warning("No article data to save. Skipping...")
            return False

        try:
        #Insert the article into the database
            self._logger.info(f"Saving article to database: {article['title']}")
            insert_query = """
                INSERT INTO wiki_articles (title, summary, image_url)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(insert_query, (article['title'], article['summary'], article['image_url']))
            self.connection.commit() # Commit the transaction
            self._logger.info(f"Article '{article['title']}' saved successfully.")
            return True
        except mariadb.Error as e:
            self._logger.error(f"Error saving article '{article['title']}': {e}")
            self.connection.rollback() #Rollback on error
            return False

    def run(self):
        """
        Executes function for the crawler. Ensures cleanup of resources at the end.
        """
        self._logger.info("Crawler started.")
        try:
            crawl_list = self.get_crawl_list()

            for url in crawl_list:
                article = self.crawl(url)
                if article:
                    self.save(article)

        except Exception as e:
            self._logger.error(f"Unexpected error during crawling: {e}")
        finally:
            # Ensure the database connection is closed properly
            if self.connection:
                self.connection.close()
                self._logger.info("Crawler finished and database connection closed.")

if __name__ == '__main__':
    crawler = WikiCrawler()
    crawler.run()