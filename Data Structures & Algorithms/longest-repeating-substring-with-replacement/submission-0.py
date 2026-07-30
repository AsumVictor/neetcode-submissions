class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = {}
        max_char = 0
        l = 0
        max_sequence = 0
        for r in range(len(s)):

            # add to the freq
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_char = max(max_char, freq[s[r]])

            # invalid window
            while l < len(s) and ((r - l + 1) - max_char) > k:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
            
            max_sequence = max(max_sequence, (r - l + 1))


        return max_sequence

            
            