# Gopher2rss

This is a python script designed for use with GitHub pages which coverts a
gophermap of a directory into a rss feed.

## Usage
In the gopher2rss.cfg file, you can put the url to any gopher page like so:
```
host directory
tilde.club /1/~user18130814200115/posts
```
The space between the host and the directory is very important.

The script will then produce an xml file for every text entry in the directory
(currently does not work if the directory contains other gophermaps). It will
also create an index.html file for easy aces to the generated feeds.

The script will not scrape any posts already present in the feed to save on
bandwith.

## Dependencies
The script is written in python 3 and additionally uses curl. Libraries used are
`os` and `html`.

## Copyright
I am not liable if anyone uses this script to scrape and host copyrighted content. Host generated feeds publicly only with permission from the author.
