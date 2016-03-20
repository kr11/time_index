__author__ = 'kangrong'
# 26 letters of alphabet are limit in the breadth for SAX
import copy
import types
from conf import *

class StringEx:
    def __init__(self, strings):
        self.size = 0
        self.strings = []
        if type(strings) is types.IntType:
            self.strings = [strings]
            self.size += 1
        elif type(strings) is types.ListType:
            self.strings = strings
            self.size = len(strings)
        elif type(strings) is types.StringType:
            for i in strings:
                self.strings.append(ord(i))
            self.size = len(strings)


    def char_at(self, i):
        return self.strings[i]

    def __add__(self,other):
        ret = copy.deepcopy(self)
        if type(other) is types.IntType:
            ret.strings.append(other)
            ret.size += 1
        elif type(other.strings) is types.ListType:
            ret.strings += other.strings
            ret.size += other.size
        return ret

    def print_line(self):
        print self.strings

    def getSize(self):
        return self.size

    # def size(self):
    #     return self.size

    def equals(self,n):
        v = n.get_value()
        if len(v) != len(self.strings):
            return False
        else:
            for i in range(len(v)):
                if v[i] != self.strings[i]:
                    return False
            return True

    def substring(self, i, end = None):
        if end is None:
            return StringEx(self.strings[i:])
        else:
            return StringEx(self.strings[i:end])

    def isEmpty(self):
        return self.size == 0

    def get_value(self):
        return self.strings

    def startsWith(self, prefix,offset = 0):
        p_string = prefix.get_value()
        s_string = self.strings
        p_off = 0
        s_off = offset
        pc = len(p_string)
        if (offset < 0) or (len(s_string) - len(p_string) < offset):
            # print (len(s_string) - len(p_string))
            return False
        while (pc > 0):
            if p_string[p_off] != s_string[s_off]:
                # print p_off
                return False
            p_off += 1
            s_off += 1
            pc -= 1
        return True

    def __str__(self):
        a = ","
        if PRINT_EN:
            ret = ""
            for i in self.strings:
                ret += chr(i)+a
            return ret
        else:
            return a.join(map(str,self.strings),)


# a = StringEx([1,2,3,4])
# b = StringEx([2,3])
# print a.startsWith(b,1)
#print a[1:0]
# a = StringEx([0,2,4])
# a.print_line()
# b = StringEx([1,3,5])
# b.print_line()
# c = a + b
# c.print_line()
# a.print_line()
