# Scrapy-Data-using-Pythone
using scrapy Library and Spider Tool to get Data from a Website 

# Requirements to run this script
1. Python 3
2. scrapy (pip install scrapy)

Step 2: open terminal
Step 3: cd to the extracted folder

# To generate json output enter this:

scrapy crawl mycrawler -o result.json

# To generate csv output enter this:

scrapy crawl mycrawler -o result.csv


# How to change image download path:

Step 1: Go to settings.py
Step 2: At the bottom change the value of "IMAGES_STORE" and save.


# How to change url to scrape:
Step 1: Open ss/spiders/crawling_spider.py
Step 2: Change the url in line 17
Step 3: Change the domain in line 16 
Step 4: Change the Rule LinkExtractor in line 21

# How to change the Data Path :
Step 1 : Open ss/items.py
Step 2 : set the class and the Items that you need 
Step 3 : Open ss/spiders/crawling_spider.py and follow my strecture , if you understand it change the Data Set
Step 4 : If you don't get any result and you got Lost Follow this Video :
https://www.youtube.com/watch?v=m_3gjHGxIJc
