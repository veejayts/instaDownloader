import urllib
from urllib import request
from bs4 import BeautifulSoup as bs
import datetime

def makeSoup(url):
	link = urllib.request.urlopen(url)
	soupMade = bs(link, "html.parser")
	return soupMade

def downloadImage(soup):
	for metaTag in soup.findAll("meta", {"property":"og:image"}):
		print("Getting the url of the image")
		Picture = metaTag.get("content")
		print("Got it!")
		print("Naming the file")
		fileName = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
		print("Saving the file in the same directory")
		imageFile = open(fileName + ".jpeg", "wb")
		print("Reading the image")
		imageFile.write(urllib.request.urlopen(Picture).read())
		print("Done")
		imageFile.close()

url = input("Enter the URL : ")
print("Thank You")

soup = makeSoup(url)
print("Done parsing the website")

downloadImage(soup)

print("Thank you for using me!")