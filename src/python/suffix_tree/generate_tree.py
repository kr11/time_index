__author__ = 'kangrong'

from node import *
class SuffixTree:
    def __init__(self):
        self.activeLeaf = Node()
        self.root = Node()

    def put(self, str, index):
        self.activeLeaf = self.root
        remainder = str
        text = StringEx([])
        # for i in range(remainder.size()):
            # text +=






