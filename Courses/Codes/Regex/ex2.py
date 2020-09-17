# coding : utf-8

import re
"""
handler = open('../mbox-short.txt')
for line in handler :
    line = line.rstrip()
    if re.search('From:',line):
        print(line)
"""

handler = open('../mbox-short.txt')
for line in handler:
    line = line.rstrip()
    if re.search('^From:',line):
        print(line)


