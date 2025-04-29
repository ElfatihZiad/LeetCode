from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
        

if __name__ == "__main__":
    solution = Solution()
    
    # Example test cases
    print(solution.containsDuplicate([1,2,3,1]))  # Expected output: true
    print(solution.containsDuplicate([1,2,3,4]))  # Expected output: false
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected output: true
