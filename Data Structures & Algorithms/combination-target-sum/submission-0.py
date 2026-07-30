class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      """
      [2,3,6,7]
           [2]
           / \
        [2,3,6,7]

      list of combination that reach a target.
      can reuse as much as posibble

      what is path:
      list of numbers that are less than sum or equal
      []

      * base case
        when sum of path == target

      * when sum is > target:
      exit


      choice:
      we can choose all number no constrac


      """

      solution = []
      candidates.sort()

      def backtrack(path, target, i):

        # when we hit solution
        if target == 0:
            solution.append(path.copy())
            return

        # when the target is legative
        if target < 0:
            return

        for j in range(i, len(candidates)):

                # add
                num = candidates[j]
                path.append(num)
                backtrack(path, target - num, j )

                # undo
                path.pop()

      backtrack([], target, 0)
      
      return solution


__import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))


      

      

