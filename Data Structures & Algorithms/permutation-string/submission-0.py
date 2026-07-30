class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)

        if (n1 > n2):
            return False

        # build count for s1
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1
        
        # go through s2 with a fixed len of s2
        s2_freq = {}
        for i in range(n1):
             s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1

        if s2_freq == s1_freq:
            return True

        for i in range(1, n2 - n1 + 1):
            # add to 
            s2_freq[s2[i - 1]] = s2_freq.get(s2[i - 1], 0) - 1
            if(s2_freq[s2[i - 1]]) <= 0:
                del s2_freq[s2[i - 1]]
            
            s2_freq[s2[i + n1 - 1]] = s2_freq.get(s2[i + n1 - 1], 0) + 1
            if s2_freq == s1_freq:
                return True

        
        return False

