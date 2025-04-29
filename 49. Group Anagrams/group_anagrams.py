from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for item in strs:
            sorted_item =  "".join(sorted(item))
            groups[sorted_item].append(item)

        return list(groups.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(s)
        
        return list(groups)

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    # Example test cases
    print(solution.groupAnagrams(strs)) 