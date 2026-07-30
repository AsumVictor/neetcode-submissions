class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """

        * ask for feasibiliy
        * sequential progression - move in one direction
        * biniry outcome
        * We dont need how

        [1,2,3,4], 
        [2,2,4,1]
        -1 0 -1 3

        gas=[1,2,3, 4,5]
        cost=[3,4,5,1,2]
        -2  -1  -2  3  3
                   ^

        do a choice of each of them

        gas= [5,1,2,3,4]
        cost=[4,4,1,5,1]
              1-3 1 -2 3


        """
        n = len(gas)
        net_gas = 0
        net_cost = [0] * n

        for i in range(n):
            # add net gas
            net_cost[i] = gas[i] - cost[i]
            net_gas += net_cost[i]
        
        # check if we can reach
        if net_gas < 0:
            return -1

        net_gas = 0
        idx = -1
        for i in range(n):

            # add net to netgas
            if net_gas == 0:
                idx = i

            net_gas = max(0, net_cost[i] + net_gas)

        
        return idx



