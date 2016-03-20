__author__ = 'kangrong'

from node import *
class SuffixTree:
    def __init__(self):
        self.activeLeaf = Node()
        self.root = Node()

    def put(self, input_str, index):
        self.activeLeaf = self.root
        remainder = input_str
        text = StringEx([])
        node = self.root
        # print remainder.size()
        for i in range(remainder.getSize()):
            text += StringEx(remainder.char_at(i))
            # print i
            node, text = self.update(node, text, remainder.substring(i), index)
            node, text= self.canonize(node, text)
        if self.activeLeaf.getSuffix is not None and self.activeLeaf != self.root and self.activeLeaf != node:
            self.activeLeaf.setSuffix(node)


    def update(self,input_node,string_port, rest, value):
        s = input_node
        # print input_node.__str__()
        temp_str = string_port
        new_char = string_port.char_at(-1)
        old_root = self.root
        is_end_point,r = self.test_and_split(s,temp_str.substring(0,-1),new_char,rest, value)
        while is_end_point is False:
            temp_edge = r.getEdge(new_char)
            if temp_edge is None:
                leaf = Node()
                leaf.addValueRef(value)
                newedge = Edge(rest, leaf)
                r.addEdge(new_char, newedge)
            else:
                leaf = temp_edge.getDest()

            #line 4
            if self.activeLeaf != self.root:
                self.activeLeaf.setSuffix(leaf)
            self.activeLeaf = leaf

            if old_root != self.root:
                old_root.setSuffix(r)
            old_root = r
            # line 6
            if s.getSuffix() is None:
                temp_str = temp_str.substring(1)
            else:
                # s = canret.getFirst();
                s, temp = self.canonize(s.getSuffix(), self.safeCutLastChar(temp_str))
                temp_str = (temp + temp_str.char_at(-1))

            is_end_point,r = self.test_and_split(s,temp_str.substring(0,-1),new_char,rest,value)
        #line 8
        if old_root != self.root:
            old_root.setSuffix(r)
        return s,temp_str

    def safeCutLastChar(self,tempstr):
        if (tempstr.isEmpty()):
            return tempstr
        return tempstr.substring(0, tempstr.getSize() - 1)

    def canonize(self,s,input_str):
        if input_str.isEmpty():
            return s,input_str
        else:
            current = s
            temp_str = input_str
            g = s.getEdge(temp_str.char_at(0))
            while g is not None and temp_str.startsWith(g.getLabel()):
                temp_str = temp_str.substring(g.getLabel().getSize())
                current = g.getDest()
                if temp_str.getSize() > 0:
                    g = current.getEdge(temp_str.char_at(0))
            return current,temp_str

    def test_and_split(self, inputs, stringPart, t, remainder, value):
        s,temp_str = self.canonize(inputs,stringPart)
        if temp_str.isEmpty() is False:
            g = s.getEdge(temp_str.char_at(0))
            if g is None:
                print 123
            l = g.getLabel()
            if l.getSize() > temp_str.getSize() and l.char_at(temp_str.getSize()) == t:
                return True,s
            else:
                # it should be splited
                new_label = l.substring(temp_str.getSize())
                new_node = Node()
                new_edge = Edge(temp_str,new_node)
                s.addEdge(temp_str.char_at(0),new_edge)
                g.setLabel(new_label)
                new_node.addEdge(new_label.char_at(0),g)
                return False,new_node
        else:
            edge = s.getEdge(t)
            if edge is None:
                return False,s
            else:
                label = edge.getLabel()
                if remainder.equals(label):
                    #add ref
                    edge.getDest().addValueRef(value)
                    return True,s
                elif remainder.startsWith(label):
                    return True,s
                elif label.startsWith(remainder):
                    # label.startsWith(remainder)
                    #it means the edge's label contains the whole string for remainder,
                    #thus it should be splited at position of label
                    #split
                    new_label = label.substring(remainder.getSize())
                    new_node = Node()
                    new_node.addValueRef(value)
                    new_edge = Edge(remainder,new_node)
                    s.addEdge(t,new_edge)
                    edge.setLabel(new_label)
                    new_node.addEdge(new_label.char_at(0),edge)
                    return False,s
                else:
                    return True,s

    def search(self,ex_string,num = -1):
        node = self.search_node(ex_string)
        if node is None:
            return []
        else:
            return node.getData(num)

    def search_node(self,ex_string):
        node = self.root
        i = 0
        while i < ex_string.getSize():
            new_char = ex_string.char_at(i)
            edge = node.getEdge(new_char)
            if edge is None:
                return None
            label = edge.getLabel()
            if label.startsWith(ex_string.substring(i)):
                return edge.getDest()
            elif ex_string.substring(i).startsWith(label):
                node = edge.getDest()
                i += label.getSize()-1
            else:
                return None
            i+=1
        return node





# leaf = Node()
# e = Edge(StringEx([1,2]),leaf)
# a = Node()
# a.addEdge(1,e)

# print a.getEdge(1) == e



