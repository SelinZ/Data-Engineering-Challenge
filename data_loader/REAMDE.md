# Optional Challenge

## Introduction

This challenge is optional, if you have finished the first challenge and would like to demonstrate your skills further, then we welcome you to try the optional challenge.

This assignment reflects another core part of our data engineering responsibilities, building ETLs to load data from external sources into internal system.

You will demonstrate your skills on data operations.

You will need to write a script which:

1. load the data in .\data_loader\example-data.xlsx into a dataframe
2. Load the data into table `trade_records`

Your solution will be assessed with the same criteria as the WikiCrawler challenge.

## Hint

1. First review the content of the file and think of what the schema of `trade_records` table should be like
2. Modify `.\database\init.sql` to include the schema for the new table
3. You need to modify `docker-compose.yml` in order to run the DataLoader and INSERT the data into mariadb
4. The content in .\data_loader folder is not complete, compare what is needed for WikiCrawler and add the missing files 
5. You could use `pandas` to load the data
6. Think of the quality of the data, are they in right data types? are there duplicates?