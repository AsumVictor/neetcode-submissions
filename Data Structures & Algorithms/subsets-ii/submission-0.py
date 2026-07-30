class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        [1,2,2]
        [[],[1],[1,2],[1,2,2],[2],[2,2]]

        a number contain duplicate:
          - no duplicates

        
        path: store nums[i] that has been repeated before

        bases case i == n: it means explore all values

                  i=0, [], {1,2,2}
                  i= 1             [2]            [3]
                  [1] - {2,3}     
                 /
             [2] {2}  \[3]
             /
          [2] - {}


          keep track of seen with string: becuase it sorted with "="
  

        """
        # sort numbers 
        nums.sort()

        solution = []
        seen = set()
        n = len(nums)

        def bracktrack(path, i):

            # return ehrn reach 
            if i == n:
                # add solution

                sol = tuple(path)
                if sol not in seen:
                    solution.append(path.copy())
                # add to seen
                    seen.add(sol)
                
                return
            
            # exlude this number
            bracktrack(path, i + 1)

            # pick this number
            path.append(nums[i])
            bracktrack(path, i + 1)
            path.pop()


            return

        
        bracktrack([], 0)

        return solution

            

