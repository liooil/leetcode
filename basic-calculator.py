class Solution:
    def calculate(self, s: 'str') -> 'int':
        def chunkiter(expr):
            integer = ""
            for c in s:
                if c in "0123456789":
                    integer += c
                else:
                    if integer:
                        yield int(integer)
                        integer = ""
                    if c in "+-()":
                        yield c
            else:
                if integer:
                    yield int(integer)
        def shunting_yard(expr):
            queue = []
            stack = []
            for chunk in chunkiter(expr):
                if chunk == '(':
                    stack.append('(')
                elif chunk == ')':
                    while stack[-1] != '(':
                        queue.append(stack.pop())
                    while stack and stack[-1] == '(':
                        stack.pop()
                elif chunk == '+':
                    stack.append('+')
                elif chunk == '-':
                    stack.append('-')
                else:
                    queue.append(chunk)
            else:
                while stack:
                    queue.append(stack.pop())
            return queue
        stack = shunting_yard(s)
        def pop_one(stack):
            chunk = stack.pop()
            if chunk == "+":
                b = pop_one(stack)
                a = pop_one(stack)
                return a + b
            elif chunk == '-':
                b = pop_one(stack)
                a = pop_one(stack)
                return a - b
            else:
                return chunk
        return pop_one(stack)

