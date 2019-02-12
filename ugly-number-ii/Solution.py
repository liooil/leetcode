class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        class Node:
            def __init__(self, x):
                self.val = x
                self.next = None
        head = tail = Node(1)
        id = {2:head, 3:head, 5:head}
        U = {2:2, 3:3, 5:5}
        for _ in range(n-1):
            umin = min(U.values())
            tail.next = Node(umin)
            tail = tail.next
            for ukey in (2,3,5):
                if U[ukey] == umin:
                    id[ukey] = id[ukey].next
                    U[ukey] = ukey * id[ukey].val
        return tail.val

if __name__ == "__main__":
    s = Solution()
    ans = s.nthUglyNumber(10)
    print(ans)