# DEPRECATED

## instaDownloader

A non-API python script that will download images and videos from public instagram profiles.

This is completely based on webcrawling.

The program downloads the webpage that the user provides, grabs the URL where the image(s)/video is stored and writes the data of that URL to a .jpeg or .mp4 file(s) in the same directory as this python file is present.

The code to download a post containing only one image or video, is straight-forward as the link is present in the meta tag.

The code to download a collection of image(s) works based on the keywords that Instagram uses in the web page. This code cannot download a collection of videos.

This is a CLI (Command Line Interface) program.
