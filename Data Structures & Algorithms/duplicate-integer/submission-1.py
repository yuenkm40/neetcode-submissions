class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initial solution
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        #optimized solution 
        return len(set(nums)) < len(nums)

        