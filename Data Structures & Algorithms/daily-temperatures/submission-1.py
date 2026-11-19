class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                day = stack.pop()
                res[day] = i - day
            stack.append(i)

        while stack:
            day = stack.pop()
            res[day] = 0
        return res

        
#30 
#38 30 
#38 36 35
#40 

#22
#22 21
#22 21 20