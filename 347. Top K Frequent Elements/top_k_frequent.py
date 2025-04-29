from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for item in nums:
            frequency[item] = frequency.get(item, 0) + 1
        
        arr = []
        for num, cnt in frequency.items():
            arr.append([cnt, num])

        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
    
    def topKFrequent_BS(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for item in nums:
            count[item] = count.get(item, 0) + 1
        
        for item, count in count.items():
            freq[count].append(item)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res