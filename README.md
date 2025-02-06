# Data Engineer Challenge

## Introduction

Implemented a wikipedia crawler, got the data then saved the results to MariaDB.

Modified the files in `database/` and `crawler/`.

Used `Git` to make commits for my changes.

## WikiCrawler Implementation Details

Designed a crawler to crawl the title, summary, and image url of certain wikipedia pages.

Implemented the `crawl` function of WikiCrawler.py. 
The `crawl` function should visit certain wikipedia pages from the crawling list and then extract the title, the summary (or first 150 words of the main content) and the image url.

Stored these information in `wiki_articles` table by implementing the `save` function of WikiCrawler.py. 
The table was expanded with fields `title`, `summary`, and `image_url` by modifying the `init.sql.` under the database folder.

The data was inserted into the mariadb instances's `wiki_articles` table using `mariadb` python library. 

## Setup and Environment

1. [Installed Docker](https://docs.docker.com/engine/install/) and [installed Docker-Compose](https://docs.docker.com/compose/install/).

2. Initalized the `data-engineer-challenge-crawler` folder with git

3. The service could be run with **`docker-compose up --build`**, stopped with **`CTRL + C`** and taken down with **`docker-compose down`**.
To clean up any containers when done, used **`docker-compose rm`**.
The **`docker-compose rm`** command was useful when modifying the database schema, as mariadb only runs the scripts found in `database/` upon the first load from a clean environment.

Used an Ubuntu 20.04 environment with python 3 to run the crawler.


### SQL

To examine the state of the mariadb tables (for both debugging and assessment), execed into the docker container by running the following commands:

```
docker exec -it data-engineer-challenge-crawler-mariadb-1 bash

mysql -u crawler -pXXX

use crawler_dev;

SELECT * FROM `wiki_articles` LIMIT 10;
```

### Git

Here is a helpful guide: [Commit Message Guidelines](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)

- Short one-liner commit message on the first line
- Detailed description in the commit message body
- Use of amending or squashing to create final commit on the master branch
- Use of git feature branches or other git workflow