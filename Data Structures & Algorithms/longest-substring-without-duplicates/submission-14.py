class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start_ptr = 0
        substring = set()

        for i, ch in enumerate(s):
            while ch in substring:
                substring.remove(s[start_ptr])
                start_ptr += 1

            substring.add(ch)
            max_length = max(i - start_ptr + 1, max_length)
            
        return max_length
            

        