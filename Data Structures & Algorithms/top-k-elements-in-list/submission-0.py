class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for num in nums:
            freqMap[num] += 1
       
        return sorted(freqMap, key = lambda x: -freqMap[x])[:k]
        