class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def f(x):
            return sum(1 for v in nums if v >= x)

        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            count = f(mid)
            if count == mid:
                return mid
            elif count > mid:
                l = mid + 1
            else:
                r = mid - 1
        return -1