__author__ = 'kangrong'
# 26 letters of alphabet are limit in the breadth for SAX
import copy
class StringEx:

    def __init__(self, strings):
        # integer array
        self.strings = strings
        self.size = len(strings)

    def char_at(self, i):
        return self.strings[i]

    def __add__(self,other):
        ret = copy.deepcopy(self)
        ret.strings += other.strings
        ret.size += other.size
        return ret

    def print_line(self):
        print self.strings

    def size(self):
        return self.size


a = StringEx([0,2,4])
a.print_line()
b = StringEx([1,3,5])
b.print_line()
c = a + b
c.print_line()
a.print_line()