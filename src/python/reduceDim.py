# coding:utf-8
__author__ = 'KangRong'

f = open('legend.csv')
legendNum = 101
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

#generate csv format file for excel showing
# t = False
# r = 0
# print 'multi'
# for i in range(0,10):
#     f_multi = open('multi_legend_'+str(i)+'_.csv','w')
#     r = 0
#     while True:
#         t = False
#         for s in range(0,10):
#             if r < len(PAAresult[i*10+s]):
#                 f_multi.write(str(PAAresult[i*10+s][r][1])+',')
#                 t = True
#             else:
#                 f_multi.write('0,')
#         f_multi.write('\r\n')
#         r += 1
#         if not t:
#             break
#     f_multi.close()

#exit()
#GAUSS
basic = 0
inter = 100
basicCharAscii = ord('A')

sax = open('SAX.csv','w')
paa = open('paa.csv','w')
for i in PAAresult:
    i = 15
    legendStr = ''
    ps = PAAresult[i]
    for tuple in ps:
        value = tuple[1]
        if value < basic:
            print 'less than basic' + str(value)
            #continue
            #exit()
        paa.write(str(i)+','+str(tuple[1])+'\n')
        legendStr += chr(basicCharAscii + (value-basic)/inter)
    print i,legendStr
    sax.write(str(i)+','+legendStr+'\n')
    break

sax.close()