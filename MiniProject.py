"""
Mini-Project Demo 
Group 2,68,71 
"""
from bs4 import BeautifulSoup
import urllib3

redditFile = urllib3.connection_from_url("http://www.reddit.com")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))