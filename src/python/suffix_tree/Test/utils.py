__author__ = 'kangrong'


def getSubstrings(strings):
    ret = set()
    for l in range(1,len(strings)+1):
        for start in range(len(strings)-l+1):
            # print l,start
            ret.add(strings[start:start+l])
    return ret

# print getSubstrings("asd")