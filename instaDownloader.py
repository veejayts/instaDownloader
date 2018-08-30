import urllib
from urllib import request
from bs4 import BeautifulSoup as bs
import datetime


def choiceCheck(choice):

	# User is prompted to enter the choice at the beginning of the program.

	if choice == "1" or choice == "2" or choice == "3":
		return True
	else: 
		return False

def userChoice():
	
	# Asking the user what they want to download so that instead of searching for seperate tags, links and 
	# keywords, the process can be completed a lot faster
	
	choice = input("Do you want to download \
		\n 1 - Single Image or \
		\n 2 - Single Video or \
		\n 3 - Collection of Images and Photos \
		\n\n Enter 1 or 2 or 3 --> ")
	return choice

def urlPrompt():
	
	# Asking the user for the URL to proceed with the program
	
	url = input("Enter the URL : ")
	print("Thank You")
	return url

def makeSoup(url):
	
	# Downloading the webpage and parsing it using BeautifulSoup so that the program can grab the links
	# of the images and videos
	try:
		link = urllib.request.urlopen(url)
		soupMade = bs(link, "html.parser")
	except Exception:
		print("Invalid URL. Please make sure that the profile is public!")
		return False
	else:
		return soupMade
	finally:
		pass

def downloadSingleImage(soup):
	
	# If there is only a single image in the instagram post, this function is called (the user provides this
	# information). The link is present directly in the meta tag.
	
	for metaTag in soup.findAll("meta", {"property":"og:image"}):
		print("Getting the url of the image")
		picture = metaTag.get("content")
		print("Got it!")
		
		print("Naming the file")
		fileName = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
		print("Saving the file in the same directory")
		imageFile = open(fileName + ".jpeg", "wb")
		
		print("Reading the image")
		imageFile.write(urllib.request.urlopen(picture).read())
		print("Done")
		imageFile.close()

def downloadSingleVideo(soup):

	# If there is only a single video in the instagram post, this function is called (the user provides this
	# information). The link is present directly in the meta tag.

	for metaTag in soup.findAll("meta", {"property":"og:video"}):
		print("Getting the url of the video")
		video = metaTag.get("content")
		print("Got it!")
		
		print("Naming the file")
		fileName = datetime.datetime.now()#.strftime("%Y %m %d %H %M %S")
		print("Saving the file in the same directory")
		imageFile = open(fileName + ".mp4", "wb")
		
		print("Reading the video")
		imageFile.write(urllib.request.urlopen(video).read())
		print("Done")
		imageFile.close()

def downloadCollection(soup):

	# If the single instagram post contains a more than one image or video or a mix of both, this function
	# is called (the user provides this information). The link is present inside the script tag which makes
	# it difficult to just grab the links. So the script tags are split from the document and converted
	# into a list. Then the program obtains the indices of particular keywords used on the website. One index
	# past the keywords, is the link of the image/video which is grabbed. This is a very inefficient way. 

	# Here the program checks the webpage for a video and downloads the videos automatically if present. If 
	# not, it downloads only the images.

	scriptTag = soup.findAll("script")
	scriptStr = str(scriptTag)
	mediaList = scriptStr.split('"')

	print("Getting the url of the image")

	#Got the line of code below from stack overflow
	imgURL = [i for i, e in enumerate(mediaList) if e == "display_url"]
	imgURL = tuple(imgURL)
	print("Got it!")

	mediaTuple = list()	
	for i in imgURL:
		mediaTuple.append(mediaList[i+2])
	mediaTuple = tuple(mediaTuple)
	
	imgNumber = 1

	for link in mediaTuple:
		print("Naming the file")
		fileName = datetime.datetime.now().strftime("%Y %m %d %H %M %S" + " " + str(imgNumber))
		print("Saving the file in the same directory")
		imageFile = open(fileName + ".jpeg", "wb")
		
		print("Reading the image")
		imageFile.write(urllib.request.urlopen(link).read())
		print("Done")
		imageFile.close()

		imgNumber += 1

	vidNumber = 1

	if "video_url" in mediaList:
		print("Getting the url of the video")

		#Got the line of code below from stack overflow
		vidURL = [i for i, e in enumerate(mediaList) if e == "video_url"]
		vidURL = tuple(vidURL)
		print("Got it!")

		videoTuple = list()
		for i in vidURL:
			videoTuple.append(mediaList[i+2])
		videoTuple = tuple(videoTuple)

		for link in videoTuple:
			print("Naming the file")
			fileName = datetime.datetime.now().strftime("%Y %m %d %H %M %S" + " " + str(vidNumber))
			print("Saving the file in the same directory")
			imageFile = open(fileName + ".mp4", "wb")
			
			print("Reading the video")
			imageFile.write(urllib.request.urlopen(link).read())
			print("Done")
			imageFile.close()

			vidNumber += 1

# This loop is present to ensure that the user is entering the correct choice so that they don't break
# the program. 

while(1):
	choice = userChoice()
	validity = choiceCheck(choice)

	if validity is False:
		print("\nDidn't quite catch that. Can you please enter your choice again? \n")
		continue
	else:
		break

# Once the user has made the choice, the user are asked to enter the URL.
url = urlPrompt()

# To download the webpage, we are calling this function.
soup = makeSoup(url)
if soup is not False:
	print("Done parsing the website")
else:
	exit()

# Now, according to the choice of the user, we are calling the respective functions
if choice == "1":
	downloadSingleImage(soup)
elif choice == "2":
	downloadSingleVideo(soup)
else:
	downloadCollection(soup)

print("\n Thank you for using me!")