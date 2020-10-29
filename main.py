from bs4 import BeautifulSoup

##use requests to get the data
import requests

##what do you want to search for?
search = input('Enter search term: ')

##set a get parameter
params = {"q": search}
##build a request
r = requests.get("https://www.bing.com/search", params=params)

##transform the requests response into beautiful soup to be readable
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

