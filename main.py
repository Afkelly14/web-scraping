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
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

##put links in a for statement and print if they have certain attributes
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

