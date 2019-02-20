class Solution:
    def asteroidCollision(self, asteroids: 'List[int]') -> 'List[int]':
        Rs = []
        Ls = []
        for a in asteroids:
            if a > 0:
                Rs.append(a)
            else:
                while Rs:
                    b = Rs.pop()
                    if -a > b:
                        continue
                    elif -a < b:
                        Rs.append(b)
                        break
                    else:
                        break
                else:
                    Ls.append(a)
        return Ls + Rs