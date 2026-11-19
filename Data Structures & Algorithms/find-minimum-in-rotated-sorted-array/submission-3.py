class Solution:
    [3,4,5,6,7,1,2]
    def findMin(self, nums: List[int]) -> int:
        #O(n)
        # return min(nums)
        left, right = 0, len(nums) - 1
        min_num = 1000
        while left < right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                min_num = min(min_num, nums[left])
                left = mid + 1
            else:
                if nums[mid] < nums[right]:
                    min_num = min(min_num, nums[mid])
                    right = mid -1 
               
        return min(min_num, nums[right])


        