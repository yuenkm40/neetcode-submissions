class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                start = num
                length = 1
                while (start + length) in numSet:
                    length += 1
                if length > longest:
                    longest = length
        
        return longest 

        