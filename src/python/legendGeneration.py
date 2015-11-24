# coding:utf-8
__author__ = 'KangRong'

import random

f = open('test_out.csv','r')
lineCount = 10613570
#lineCount = 1000
line = f.readline()


legendNum = 100
#legendNum = 10
maxLen = 300
minLen = 200

#生成图例的起止点
legendEndPoints = []
i = 1
# while True:
#     start = random.randint(1, lineCount)
#     end = start + random.randint(minLen,maxLen)
#     if end > lineCount:
#         continue
#     if (start,end) not in legendEndPoints:
#         legendEndPoints.append((start,end))
#         i += 1
#     if i > legendNum:
#         break
legendEndPoints.append((200,399))
legendNum = 1
i = 0
legendPoints = {}
while line != '':
    i += 1
    st = line[:-1].split(',')
    time = st[0]
    value = st[1]
    for s in range(0,legendNum):
        tuple = legendEndPoints[s]
        if i >= tuple[0] and i <= tuple[1]:
            if s not in legendPoints:
                legendPoints[s] = []
            legendPoints[s].append(line)
    line = f.readline()
    if i % 10000 == 0:
        print i


out = open('legend1.csv','w')
for i in legendPoints:
    ps = legendPoints[i]
    for ln in range(0,len(ps)):
        out.write(str(i)+',')
        out.write(ps[ln])
