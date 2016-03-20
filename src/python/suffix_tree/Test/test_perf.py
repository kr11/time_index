__author__ = 'kangrong'

def test_sort():
    data = []


def getContain_binary(self,value,data):
    low = 0
    high = self.dataSize-1
    while low < high:
        mid = (low + high)>>1
        if value < self.data[mid]:
            high = mid - 1
        elif value > self.data[mid]:
            low = mid + 1
        else:
            return True
    return False