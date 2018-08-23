import urllib
from urllib import request
from bs4 import BeautifulSoup as bs
import json

def makeSoup(url):
	link = urllib.request.urlopen(url)
	soupMade = bs(link, "html.parser")
	return soupMade

url = input("Enter the URL: ")
soup = makeSoup(url)

scriptTag = soup.findAll("script")

print(scriptTag)
scriptTag = str(scriptTag)

jsonFile = json.dumps(scriptTag)

yaas = json.loads(jsonFile)

yaas.split(",")

if "display_url" in yaas:
	print("Yea")
	print(indexof("display_url"))
else:
	print("nope")