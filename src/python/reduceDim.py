# coding:utf-8
__author__ = 'KangRong'

f = open('legend1.csv')
legendNum = 1
avgSegLen = 10
line = f.readline()

PAAresult = {}
for i in range(0,legendNum):
    PAAresult[i] = []
id = 0
ic = 0
sum = 0
time = 0



while line != '':
    st = line[:-1].split(',')

    if int(st[0]) == id:
        ic += 1
        sum += int(st[2])
        if ic ==avgSegLen:
            print ic
            PAAresult[id].append((time, sum/avgSegLen))
            ic = 0
            sum = 0
    elif ic != 0:
        id += 1
        print id
        PAAresult[id].append((time, sum/ic))
        ic = 0
        sum = int(st[2])
    else:
        id += 1
        print id
        ic=1
        sum = int(st[2])
    if ic == 1:
        time = st[1]
    line = f.readline()

#GAUSS
basic = 300
inter = 20
basicCharAscii = ord('A')

sax = open('SAX.csv','w')
paa = open('paa.csv','w')
for i in PAAresult:
    legendStr = ''
    ps = PAAresult[i]
    for tuple in ps:
        paa.write(str(i)+','+str(tuple[1])+'\n')
        value = tuple[1]
        if value < basic:
            print 'less than basic' + str(value)
            exit()
        legendStr += chr(basicCharAscii + (value-basic)/inter)
    print i,legendStr
    sax.write(str(i)+','+legendStr+'\n')


sax.close()