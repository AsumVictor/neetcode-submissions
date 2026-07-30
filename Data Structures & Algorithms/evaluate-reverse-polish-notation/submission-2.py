class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["1","2","+","/","3","*","/","4","-"]
                          ^
        [3]

        if not operator:
            add list
        else:
            last = recent added: 2
            first = last but one: 1
            result = operation(operator,first, last ): +,1, 2
            result: 3
            

        operation:
           - 

        stack: 3

        num2: 2
        num1: 1
        result: 3
        """

        operators = set({"+", "-", "*","/"})

        def operation(operator, num1, num2):
            if operator == "+":
                return num1 + num2

            if operator == "-":
                return num1 - num2

            if operator == "/":
                return num1 / num2

            return num1 * num2
        
        stack = []

        for sym in tokens:

            if sym in operators:

                num2 = stack.pop()
                num1 = stack.pop()
                result = operation(sym, int(num1), int(num2))
                stack.append(result)
            else:
                stack.append(sym)

        
        return int(stack.pop())
            