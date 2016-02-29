__author__ = 'kangrong'

f = open('test.output')

fs = open('test_out.csv','w')
line = f.readline()
while line != '':
    st = line[:-1].split(',')
    if st[1].isdigit():
        fs.write(line)
    line = f.readline()

