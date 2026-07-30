class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        4: miles 2spped : 
            3 miles
        1: 3miles:
           
    
        4: 3 miles
        1: 9.5 miles
        0: 10 miles
        7: 3 miles
        A    B    C   D

        if have same distace they are fleet.



        """
        
        cars = [[pos, speed] for pos, speed in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        for pos, speed in cars:
            time_to_reach_destination = (target - pos) / speed

            if not stack:
                stack.append(time_to_reach_destination)

            elif time_to_reach_destination > stack[-1]:
                    stack.append(time_to_reach_destination)
        
        return len(stack)





