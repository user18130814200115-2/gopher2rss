# Gopher2rss

This is a python script which coverts a gophermap of a directory into a rss
feed.

## Deployments
There are many ways in which you can run this script, here are some examples:

### GitHub
This repository is set up for use with GitHub pages and CI. Feeds are checked
at midnight UCT and pushed to GitHub pages.

### Local
You can run the script locally before launching your rss reader.

### CGI
The script can easily be modified to run as a CGI script to be queried by
your RSS reader of choice.

## Usage
In the gopher2rss.cfg file, you can put the url to any gopher page like so:
```
host directory
tilde.club /1/~user18130814200115/posts
```
The space between the host and the directory is very important.

The script will then produce an xml file for every text entry in the directory
(currently does not work if the directory contains other gophermaps).

## Dependencies
The script is written in python 3 and additionally uses curl. Libraries used are
`os`, `sys` and `html`.

## Copyright
I am not liable if anyone uses this script to scrape and host copyrighted
content. If this repository contains your content and you wish for it to be
removed, please send me a message, issue, pull request, email, or courier
pigeon.

Credit to the phlogs aggregated in this repo are goes to:

Luxferre at hoi.st/1/posts  
Alex Karle at alexkarle.com/1/phlog  
Xiu at rawtext.club:70/1/~xiu/phlog  

