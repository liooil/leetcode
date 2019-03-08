class MyCalendarTwo:

    def __init__(self):
        self.first = []
        self.second = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.second:
            if start < e and end > s:
                return False
        for s, e in self.first:
            if start < e and end > s:
                self.second.append((
            max(start, s),
            min(end, e)
        ))
        self.first.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)