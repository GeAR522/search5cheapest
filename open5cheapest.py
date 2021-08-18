#!python3

import urllib.request
import webbrowser
from bs4 import BeautifulSoup as bs
import re


URL = 'https://www.places.je/propertysearch/residential-rent?propertyCategoryId=2&type=2&type=5&type=3&type=4&parish=4&sortBy=price-asc'
page = urllib.request.urlopen(URL)

soup = bs(page, features='lxml') # the base website we are searching on being made into a soup object

strongPage = soup.body.findAll('strong') #searching the bold items as th eprices are bold
function_Page = re.findall('£\d.\d+', str(strongPage)) #within thebold, searching for a price using regex


linkPage = soup.body.findAll('a')  #searching base page for all tags with 'a'
hrefPage = re.findall('property/.....', str(linkPage))  # finding the property tag, which is also link ending

for props in hrefPage[1:6]:
    urltoOpen = f'https://www.places.je/{props}'
    webbrowser.open(urltoOpen)






