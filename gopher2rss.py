#!/usr/bin/env python3

import os
import html

directory = 'docs/'

urls = []
with open('gopher2rss.cfg') as config_file:
    for line in config_file:
        urls.append(line[:-1].split(' '))
print(urls)

rss_footer = '''
</channel></rss>
'''

for url in urls:
    full_url = 'gopher://' + ''.join(url)
    filename = directory + ''.join(filter(str.isalnum, full_url)) + '.xml'

    articles_present = []
    articles_present_contents = []
    try:
        with open(filename, 'r+') as rss_file:
            for line in rss_file:
                articles_present_contents.append(line)
                if line[:6] == '<link>':
                    articles_present.append(line[6:-8])
    except:
        open(filename, 'w+')

    data = os.popen("curl -s " + full_url).read()[:-1].split('\n')

    rss_header = '''\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
<title>''' + full_url + '''</title>
<link>''' + full_url + '''</link>
'''
    rss_items = ''.join(articles_present_contents[5:-1])

    for article in data:
        if article[0] == '0':
            header = article.split('\t')
            article_url = 'gopher://' + url[0] + '/1' + header[1]
            if article_url in articles_present:
                print(article_url + " is already present in " + filename)
            else:
                contents = os.popen("curl -s " + article_url).read().split('\n')
                rss_items += '''
<item>
<link>''' + article_url +  '''</link>
<title>''' + header[0][1:] + '''</title>
<description><![CDATA[<pre>\n''' + html.escape('\n'.join(contents)) + '''</pre>]]></description>
</item>'''
    with open(filename, 'w') as rss_file:
        rss_file.write(rss_header + rss_items + rss_footer)
