class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        start at index 0
        start at index 1

        take an index:
           if index is more than N
              return 0 cost
            

            get cost of the current
            get the cost return from 1 step and two step
            get the minium of them and return

        
        input(index):

          if index >= n:
            return 0

          cost_step_1 = input(index + 1) + cost[index]
          cost_step_2 = input(index + 2) + cost[index]

          return min(cost_step_1, cost_step_2)

        
        optimization 1 is memo
        
        relationship:
        variable is index

        min cost of i = min(i -1, i - 2) + cost[i]
        [0, 2]


        '''
        
        N = len(cost)
        memo = {}
        if N <= 2:
            return min(cost)
        
        def get_cost(i):

            if i >= N:
                return 0
            
            if i in memo:
                return memo[i]

            cost_1_step = get_cost(i + 1) + cost[i]
            cost_2_step = get_cost(i + 2) + cost[i]
            memo[i] = min(cost_1_step, cost_2_step)

            return memo[i]
        
        return min(get_cost(0), get_cost(1))
            

        