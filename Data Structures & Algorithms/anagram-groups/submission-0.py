class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for str in strs:
            sortstr = ''.join(sorted(str))
            words[sortstr].append(str)
        return list(words.values())
                
                
                
        