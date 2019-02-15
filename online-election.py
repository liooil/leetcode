import bisect, collections
class TopVotedCandidate:

    def __init__(self, persons: 'List[int]', times: 'List[int]'):
        self.times = times
        def generates(persons):
            maxC, maxP = 0, None
            cnt = collections.Counter()
            for p in persons:
                cnt[p] += 1
                if cnt[p] >= maxC:
                    maxC, maxP = cnt[p], p
                yield maxP
        self.ans = []
        self.it = generates(persons)

    def q(self, t: 'int') -> 'int':
        idx = bisect.bisect(self.times, t)
        while idx > len(self.ans):
            self.ans.append(next(self.it))
        return self.ans[idx-1]
    
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

for cmd, args in zip(
    ["TopVotedCandidate","q","q","q","q","q","q"],
    [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]):
    if cmd == "TopVotedCandidate":
        persons, times = args
        s = TopVotedCandidate(persons, times)
    elif cmd == 'q':
        (t,) = args
        ans = s.q(t)
        print(ans)