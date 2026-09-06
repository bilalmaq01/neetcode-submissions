class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bigdict = {}
        freq = [[] for _ in range(len(nums)+ 1)]
        for num in nums:
            bigdict[num] = bigdict.get(num,0) + 1
        
        for meow, kitty in bigdict.items():
            freq[kitty].append(meow)
        
        meowkitty = []
        for i in range(len(freq) - 1, 0 ,-1):
            for n in freq[i]:
                meowkitty.append(n)
                if len(meowkitty) == k:
                    return meowkitty
        

