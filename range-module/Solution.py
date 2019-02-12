import bisect
class RangeModule:

    def __init__(self):
        self.data = [] # [left0, right0, left1, right1, ...]

    def getPos(self, x, isOdd):
        r = bisect.bisect(self.data, x)
        return r if r % 2 == isOdd else bisect.bisect_left(self.data, x)

    def addRange(self, left: 'int', right: 'int') -> 'None':
        l, r = self.getPos(left, 1), self.getPos(right, 1)
        del self.data[l:r]
        if l % 2 == 0:
            self.data.insert(l, left)
            if r % 2 == 0:
                self.data.insert(l+1, right)
        elif r % 2 == 0:
            self.data.insert(l, right)
        
    def queryRange(self, left: 'int', right: 'int') -> 'bool':
        l_idx = bisect.bisect(self.data, left)
        r_idx = bisect.bisect_left(self.data, right)
        return l_idx % 2 == 1 and l_idx == r_idx

    def removeRange(self, left: 'int', right: 'int') -> 'None':
        l, r = self.getPos(left, 0), self.getPos(right, 0)
        del self.data[l:r]
        if l % 2 == 1:
            self.data.insert(l, left)
            if r % 2 == 1:
                self.data.insert(l+1, right)
        elif r % 2 == 1:
            self.data.insert(l, right)

if __name__ == "__main__":
    cmds = ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
    args = [[],[10,20],[14,16],[10,14],[13,15],[16,17]]
    for cmd, arg in zip(cmds, args):
        if cmd == "RangeModule":
            obj = RangeModule()
            ans = None
        else:
            l, r = arg
            if cmd == "addRange":
                ans = obj.addRange(l, r)
            elif cmd == "removeRange":
                ans = obj.removeRange(l, r)
            elif cmd == "queryRange":
                ans = obj.queryRange(l, r)
        print(ans)