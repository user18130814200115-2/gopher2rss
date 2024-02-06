# Gopher2rss

This is a python script which coverts a gophermap of a directory into a rss
feed.

## Deployments
There are many ways in which you can run this script, here are some examples:

### GitHub
This repository is set up for use with GitHub pages and CI. Feeds are checked
every three hours and pushed to GitHub pages.

### Local
You can run the script locally before launching your rss reader.

### CGI
The script can easily be modified to run as a CGI script to be queried by
your RSS reader of choice.

## Usage
In the gopher2rss.cfg file, you can put the url to any gopher page like so:
```
tilde.club /1/~user18130814200115/posts
```

The script will then produce an xml file for every text entry in the directory. If the entry is a gophermap rather than a text file, the script tries to estimate if the map is a directory or a post by counting the number of links as opposed to the number of info lines. If the number of info lines is greater, then we process the gophermap as a post, trunign the gopher links into html ones.

## Dependencies
The script is written in python 3 and additionally uses curl. Libraries used are
`os`, `sys` and `html`.

## Copyright
I am not liable if anyone uses this script to scrape and host copyrighted
content. If this repository contains your content and you wish for it to be
removed, please send me a message, issue, pull request, email, or courier
pigeon.

Credit to the phlogs aggregated in this repo are goes to:

Luxferre at hoi.st/1
Alex Karle at alexkarle.com/1 
Xiu at rawtext.club/1/~xiu 
James Tomasino at gopher.black/1
