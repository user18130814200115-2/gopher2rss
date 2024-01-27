#!/usr/bin/env python3

import os
import sys
import html

# Initialize variable defaults
directory = './'
config_path = 'gopher2rss.cfg'
urls = []
articles_present = []
articles_present_contents = []
rss_footer = '</channel></rss>'

# By default, run verbosely
def prints(data):
    print(data)
# By default, run silently
def printv(data):
    pass

# This is the main function, it takes a url for a gopherhole, parses its contents to xml and writes them to a file
def check(url):
    new_posts = 0
    prints('Checking ' + url)
    # Add the protocol
    full_url = 'gopher://' + url
    # This is the name of the file where we store the rss feed. It is simply the url stripped of all special characters 
    filename = directory + ''.join(filter(str.isalnum, full_url)) + '.xml'

    # See if there is already a feed for the current url
    try:
        # If there is, store its contents, also store the link to every post in a separate list
        with open(filename, 'r+') as rss_file:
            for line in rss_file:
                articles_present_contents.append(line)
                if line[:6] == '<link>':
                    articles_present.append(line[6:-8])
    except:
        # If there is no feed present, create an empty xml file
        open(filename, 'w+')

    # Read the directory gophermap as a list for easy iteration
    data = os.popen("curl -s " + full_url).read()[:-1].split('\n')

    # Generate the rss header
    rss_header = '''\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>''' + full_url + '''</title>
<link>''' + full_url + '''</link>
'''
    # Store the articles already present in a variable, we will append new posts to this variable later.
    rss_items = ''.join(articles_present_contents[5:-1])

    # Loop over every line in the gophermap
    for article in data:
        # If the entry is a text file, continue
        if article[0] == '0':
            # Gophermaps contain information separated by tab characters as `name location host port`
            header = article.split('\t')
            # From this header we can reconstruct the url for the given post
            article_url = 'gopher://' + header[2] + '/1' + header[1]
            # Check if the article is already present in the rss feed.
            if article_url not in articles_present:
                new_posts += 1
                contents = os.popen("curl -s " + article_url).read()
                new_item = '''
<item>
<link>''' + article_url +  '''</link>
<title>''' + header[0][1:] + '''</title>
<description><![CDATA[<pre>\n''' + html.escape(contents) + '''</pre>]]></description>
</item>'''
                rss_items += new_item
                printv(new_item)

    # If there are new posts, write the full data to the xml file
    if new_posts > 0:
        prints('Writing ' + str(new_posts) + ' new posts to ' + filename)
        with open(filename, 'w') as rss_file:
            rss_file.write(rss_header + rss_items + rss_footer + '\n')
    else:
        prints('No new posts')


# Main loop
# Parse command line switches
for argument in sys.argv:
    match argument:
        case '-s':
            def prints(data):
                pass
        case '-c':
            config_path = argument
        case '-o':
            directory = argument
        case '-p':
            def printv(data):
                print(data)
        case '-h':
            print('''\
Usage: gopher2rss [options...]
-h, --help      Print this help message, then exit
-s, --silent    Do not output verbose messages
-c, --config    Location of the configuration file, defaults to gopher2rss.cfg
-o, --output    Directory to output the xml files to, defaults to `./`, can also be set in configuration file.
-p, --print     Print the rss data for all new articles to the console, Recommend to be used with -s

Configuration:
The configuration file contains the urls for the gopher directories you wish to aggregate importantly WITHOUT the `gopher://` protocol string.
If a line starts with a hash symbol followed by a single space, it is read as containing the output directory. If this value is set, it will overwrite the value set by `-o` or `--output`.
            ''')
            sys.exit()

# Here we read the configuration file
prints("Reading configuration file")
with open('gopher2rss.cfg') as config_file:
    for line in config_file:
        # If the line starts with a hash it contains the output directory value
        if line[0] == '#':
            directory = line[2:-1]
            prints('Setting output directory to ' + directory)
        # Otherwise, it contains a url
        else:
            urls.append(line[:-1])
# Loop over every gopherhole we are aggregating
for url in urls:
    check(url)
