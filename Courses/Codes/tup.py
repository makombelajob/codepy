# coding : utf-8

name = input('Enter file name : ')
handler = open(name)

dc = {}
tp = []

for line in handler :
    words= line.split()
    for word in words:
        dc[word] = dc.get(word,0)+1
    
for k,v in dc.items():
    tp.append((v,k))

tp = sorted(tp, reverse=True)
for v,k in tp[:10]:
    print(k,v)