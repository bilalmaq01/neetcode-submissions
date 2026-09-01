class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev = {}

        for i,n in enumerate(nums):
            needed = target - n
            if (needed in prev):
                return [prev[needed],i]
            prev[n] = i
        
        