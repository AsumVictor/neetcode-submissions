class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        lt
        lb
        rt
        rb


        """
        n = len(matrix) - 1
        l = 0
        r = n

        row_index = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row_index = mid
                break
            
            if matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        if row_index == -1:
            print("HERE")
            return False

        lt = 0
        rt = len(matrix[0]) - 1

        while lt <= rt:
            mid = (lt + rt) // 2

            if matrix[row_index][mid] == target:
                return True

            if matrix[row_index][mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1

        
        return False



