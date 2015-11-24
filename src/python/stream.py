# coding:utf-8
__author__ = 'KangRong'

from global_var import *
global data_dir

f = open(data_dir + 'test_out.csv')
#f = open('test1')
legendNum = 10
avgSegLen = 20
line = f.readline()
PAAresult = {}
for i in range(0,legendNum):
    PAAresult[i] = []
id = 0
ic = 0
sum = 0
time = 0

basic = 300
inter = 20
basicCharAscii = ord('A')

stream = ""

while line != '':
    st = line[:-1].split(',')
    ic += 1
    if st[1] == '':
        print line
        line = f.readline()
        continue
    sum += int(st[1])
    if ic ==avgSegLen:
        #print ic
        c = chr(basicCharAscii + (sum/avgSegLen-basic)/inter)
        #print c
        stream += c
        ic = 0
        sum = 0
    line = f.readline()

#print stream to file
streamf = open('stream.txt','w')
for i in range(0,len(stream)):
    streamf.write(stream[i])
    if i%10 == 0:
        streamf.write("\n")
streamf.close()

straa = 'FEDDCDFEDD'

#stream = 'FEDCCDFEDD'
#straa = 'FEDD'
#straa = 'CGEGJNKFNSLJEHK'
fs = open('find_'+str(basic)+'_'+str(inter)+'.txt','w')
pat_len = len(straa)
pat_str = 'a'+stream[0:pat_len-1]
stream_len = len(stream)
i = pat_len-1
while True:
    if i >= stream_len:
        break
#for i in range(pat_len-1,stream_len):
    if i % 2000 == 0:
        print i
    pat_str = pat_str[1:]+stream[i]
    for l in range(len(straa)-1,len(straa)+1)[::-1]:
        for s in range(0,len(straa)-l+1):
            teststring = straa[s:s+l]
            # index = pat_str.find(teststring)
            # if len(teststring) == 0:
            #     print 'sas'
            # if index != -1:
            #     fs.write(str(index+i-l)+","+teststring+"\n")
            #     print str(index+i-l)+","+teststring+"\n"
            if cmp(teststring, pat_str[0:l]) == 0:
                fs.write(str(i-pat_len+1)+","+pat_str[0:len(teststring)]+"\n")
                print str(i-pat_len+1)+","+pat_str[0:len(teststring)]
                pat_str = pat_str[l-1:]+stream[i+1:i+l]
                i += l-1
                l = -1
                break
        if l == -1:
            break
    i += 1


# for l in range(3,len(straa)):
#     for s in range(0,len(straa)-l):
#         teststring = straa[s:s+l]
#         index = stream.find(teststring)
#         if len(teststring) == 0:
#             print 'sas'
#         if index != -1:
#             fs.write(str(index)+","+teststring+"\n")
#             print str(index)+","+teststring+"\n"