#!/usr/bin/python 

import re
import sys
import requests
import time

regex = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
count = 0;
results = [] 

with open("words.txt") as file:
    words = [line.rstrip() for line in file]

print "\n"
for word in words:

    forprint = list(dict.fromkeys(results))
    for item in forprint:
     print "[*] [SCRAPED] => " + item

    while count < 99:

        if count == 55:
            print "\n[*] [DORKING] => " + word + "\n"
            time.sleep(2)
        
        url = 'https://www.bing.com/search?q='+word+'&&filt=rf&first='+str(count)
        body = requests.get(url)
        content = body.content

        links = re.findall(regex, content)

        for link in links:
        	if "microsoft" not in link:
    		    if "bing" not in link:
    		    	if "w3" not in link:
    		            results.append(link)


        count += 11
    count = 0

mylist = list(dict.fromkeys(results))
for item in mylist:
    f = open("results.txt", "a")
    f.write(item+"\n")
    f.close()












