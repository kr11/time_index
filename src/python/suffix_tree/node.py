__author__ = 'kangrong'
from ex_string import *
from edge import *
class Node:
    def __init__(self):
        self.edges = {}
        self.suffix = None
        #save the pattern index
        self.data = []

    # int char,Edge edge
    def addEdge(self,ch,edge):
        self.edges[ch] = edge

    # get edge
    def getEdge(self,ch):
        return self.edges[ch]

    #node
    def getSuffix(self):
        return self.suffix

