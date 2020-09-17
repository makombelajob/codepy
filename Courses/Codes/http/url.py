# coding : utf-8

import urllib.request, urllib.parse, urllib.error

handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in handler:
    print(line.decode().strip())