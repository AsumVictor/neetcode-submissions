class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        num1 = target[0]
        total_step = num1

        for i in range(len(target) - 1):
            if target[i] < target[i + 1]:
                total_step += target[i + 1] - target[i]

        return total_step

