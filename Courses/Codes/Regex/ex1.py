# coding : utf-8
"""
handler = open("../mbox-short.txt")
for line in handler:
    line = line.rstrip()
    #print(line)
    if line.find('From:') >= 0 :
        print(line)
"""
handler = open('../mbox-short.txt')
for line in handler:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)