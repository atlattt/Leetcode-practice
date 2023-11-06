from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        dem=1
        demmax=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    dem+=1
                else:
                    demmax=max(demmax,dem)
                    dem=1
        return max(demmax,dem)

if __name__=="__main__":
    solution=Solution()
    nums=[]
    result=solution.longestConsecutive(nums)
    print(result)