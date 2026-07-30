class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        open: 3
        close: 1

        till open == close == n
          valid parentheis

         add open when open < n
        
                    (
                   /  \
                  (    )
                 / \
                (   )
        """

        
        def generate_combination(stack, num_open, num_close):

            if num_open == num_close == n:
                print(str(stack[:]))
                result.append("".join(stack[:]))
                return

            if num_open < n:
                stack.append("(")
                generate_combination(stack, num_open + 1, num_close)
                # undo the action of add (
                stack.pop()


            if num_close < num_open:
                stack.append(")")
                generate_combination(stack, num_open, num_close + 1)
                stack.pop()

            
            return

        
        result = []
        generate_combination([], 0, 0)
        
        return result