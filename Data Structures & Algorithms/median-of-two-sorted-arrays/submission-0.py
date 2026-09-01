class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = sorted(nums1 + nums2)
        if (len(newlist)%2 == 0):
        #    meow = (float(newlist[(len(newlist)//2)-1] + float(newlist[(len(newlist)//2)])/2))
            index = len(newlist)
            answerA = newlist[int(index/2)]
            answerB = newlist[int((index/2)-1)]
            answer = (answerA + answerB) / 2
        else:
            index = len(newlist)
            answer = newlist[int(index/2)]
        #    meow = newlist[len(newlist) // 2]
        
        return float(answer)


        