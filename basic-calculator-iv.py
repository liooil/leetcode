class Solution:
    def basicCalculatorIV(self, expression: 'str', evalvars: 'List[str]', evalints: 'List[int]') -> 'List[str]':
        evalD = {vars: ints for vars, ints in zip(evalvars, evalints)}
        def shunting_yard(expression):
            ans = []
            for 