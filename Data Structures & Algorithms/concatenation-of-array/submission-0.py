class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = (len(nums)*2) * [0]
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]

        
        return ans