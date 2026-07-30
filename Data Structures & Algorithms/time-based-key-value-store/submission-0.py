"""
["foo", "bar", 1]
["foo", "bar2", 4]

foo: (bar, 1), (bar2, 4), (bar3, 10): 2
   last_index = ""

   mid <= target:
      search right
      l = mid + 1

    if mid > target:
        r = mid - 1
    


       


"""
class TimeMap:

    def __init__(self):
        self.store = {}
        
    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.store.get(key, [])
        values.append((value, timestamp))
        self.store[key] = values
        
    # O(logn)
    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        
        # check it exist

        l = 0
        r = len(values) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result
        




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)