# instaDownloader
A non-API python script that will download images and videos from public instagram profiles.

This is completely based on webcrawling. 

The program downloads the webpage that the user provides, grabs the URL where the image(s)/video(s) and writes the data of that URL to a .jpeg or .mp4 file(s) in the same directory as this python file is present.

The code to download a post containing only <strong>one</strong> image or video, is pretty simple and straight-forward as the link is present in the meta tag itself.
  
But the code to download a collection of image(s)/video(s), is not efficient. It is reliable and will work well as it is based on the keywords that Instagram uses on the webpage.

Stay dynamic,
Vijay T S
