from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

##make a loop
def StartSearch():
    ##save images from bing based on the search input
    search = input("Search for:")
    params = {"q": search}
    ##find the spaces and replace them with an underscore, make all lowercase
    dir_name = search.replace(" ", "_").lower()

    ##if this directory name is not a directory,make it one
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    ##create a request for each item in the url
    for item in links:
        try:
            img_obj = requests.get(item.attrs['href'])
            print("Getting", item.attrs["href"])
            title = item.attrs['href'].split('/')[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title, img.format)
            except:
                print("Could not save image")
        except:
            print("Could not request image")

    StartSearch()

StartSearch()