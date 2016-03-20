__author__ = 'kangrong'
from ex_string import *
# from import *
class Edge:
    def __init__(self,label, dest):
        self.label = label
        self.dest = dest

    def getLabel(self):
        return self.label

    def getDest(self):
        return self.dest

    def setLabel(self,label):
        self.label = label

    def setDest(self,dest):
        self.dest = dest

    def __str__(self):
        return "label:"+self.label.__str__()+",dest:"+self.dest.__str__()

class Node:
    def __init__(self):
        self.edges = {}
        self.suffix = None
        #save the pattern index
        self.data = []
        self.dataSize = 0

    # int char,Edge edge
    def addEdge(self,ch,edge):
        if PRINT_EN:
            ch = chr(ch)
        self.edges[ch] = edge

    # get edge
    def getEdge(self,ch):
        if PRINT_EN:
            ch = chr(ch)
        if self.edges.has_key(ch):
            return self.edges[ch]
        else:
            return None

    #node
    def getSuffix(self):
        return self.suffix

    def setSuffix(self,node):
        self.suffix = node

    def addValueRef(self,value):
        if self.getContain(value):
            return
        self.addValue(value)

        iter_suffix = self.suffix
        while iter_suffix is not None:
            if iter_suffix.getContain(value):
                return
            iter_suffix.addValueRef(value)
            iter_suffix = iter_suffix.getSuffix()


    def getContain(self,value):
        return value in self.data

        # low = 0
        # high = self.dataSize-1
        # while low < high:
        #     mid = (low + high)>>1
        #     if value < self.data[mid]:
        #         high = mid - 1
        #     elif value > self.data[mid]:
        #         low = mid + 1
        #     else:
        #         return True
        # return False

    def addValue(self,value):
        self.data.append(value)

    def __str__(self):
        ret = ""
        for (k,v) in self.edges.items():
            ret += "["+v.getLabel().__str__()+"],"
        return ret

    def getData(self, num = -1):
        ret = []
        for datum in self.data:
            ret.append(datum)
            if len(ret) == num:
                return ret
        for edge in self.edges.values():
            for datum in edge.getDest().getData(num - len(ret)):
                ret.append(datum)
                if len(ret) == num:
                    return ret
        return ret

# node = Node()
# dest = Node()
# st = StringEx([1,2])
# edge = Edge(st,dest)
# node.addEdge(1,edge)
# sss = node.getEdge(1)
# sss.setLabel(StringEx([1,2,3]))
#
# print node.getEdge(2)
