class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        zeros = nums.count(0)
        if zeros > 1:
            res = [0] * len(nums)
        elif zeros == 1:
            prod = math.prod(num for num in nums if num != 0)
            res = [prod if num == 0 else 0 for num in nums]
        else:
            # prod = math.prod(nums)
            #with division
            #res = [int(prod/num) if num != 0 else prod for num in nums]        
            #without division [O(n^2)]
            # for idx, num in enumerate(nums):
            #     res.append(math.prod(nums[:idx] + nums[idx+1:]))
            
            #without division [O(n)]
            left = 1
            for i in range(n):
                res[i] = left
                left *= nums[i]
            
            right = 1
            for j in range(n-1, -1, -1):
                res[j] *= right
                right *= nums[j]
       
        return res