class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {}

        l = 0
        max_length = 0
        for i in range(len(s)):

            # add to list
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1

            while l < len(s) and len(hashmap) != (i - l + 1):
                hashmap[s[l]] = hashmap.get(s[l], 0) - 1

                if hashmap[s[l]] <= 0:
                    del hashmap[s[l]]
                
                l += 1

            max_length = max(i - l + 1, max_length)

        
        return max_length
            