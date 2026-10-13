#-------------------------------------------------------------------------
# AUTHOR: Albert Huynh
# FILENAME: scraper.py
# SPECIFICATION: crawls the Circular Links section of TestingURL.dev starting from the seed URL
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 2 hours
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
frontier = [seed]   #waiting to be visited
seen = [seed]       #already found

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Printing the text contained in the <h1> element
    print(soup.h1.get_text())

    # Extracting and processing hyperlinks
    links = []

    for a in soup.find_all("a"):
        href = a.get("href")

        if href:
            if href.startswith("http"):
                link = href
            else:
                link = baseURL + href

            if link.startswith(seed):
                links.append(link)

    links.sort()

    for link in links:
        if link not in seen:
            seen.append(link)
            frontier.append(link)

# Printing all URLs in seen
for url in seen:
    print(url)