__author__ = 'kangrong'
import datetime

f = open('nocycle.csv')

fs = open('out_nocycle.csv','w')
line = f.readline()
while line != '':
    st = line[:-1].split(',')
    if st[1].isdigit():
        fs.write(line)
    line = f.readline()


#f = open('test.output')
# fs = open('test_out.csv','w')
# line = f.readline()
# line = f.readline()
# new = datetime.datetime.strptime(line[:-1].split(',')[0],'%Y/%m/%d %H:%M:%S')
# i = 2
# while line != '':
#     st = line[:-1].split(',')
#     old = new
#     new = datetime.datetime.strptime(st[0],'%Y/%m/%d %H:%M:%S')
#     if(new < old):
#         print str(i-1) + ',' + oldline
#         print str(i) + ',' + line
#     # if st[1].isdigit():
#     #     fs.write(line)
#     i += 1
#     oldline = line
#     # if i % 10000 == 0:
#     #     print  i
#     line = f.readline()