class Solution:
    def getAdjs(self, s):
        for i in range(4):
            yield s[:i] + str((int(s[i]) + 1) % 10) + s[i+1:]
            yield s[:i] + str((int(s[i]) - 1) % 10) + s[i+1:]
    def openLock(self, deadends: List[str], target: str) -> int:
        memo = set(deadends)
        if target in memo:
            return -1
        queue = ["0000"]
        d = 0
        while queue:
            queueN = []
            for s in queue:
                if s in memo:
                    continue
                if s == target:
                    return d
                memo.add(s)
                for ss in self.getAdjs(s):
                    queueN.append(ss)
            queue = queueN
            d += 1
        return -1