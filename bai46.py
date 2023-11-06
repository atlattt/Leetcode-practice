from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first==n:
                return result.append(nums[:])
            for i in range(first,n):
                nums[first],nums[i]=nums[i],nums[first]
                backtrack(first+1)
                nums[first],nums[i]=nums[i],nums[first]
        n=len(nums)
        result=[]
        backtrack(0)
        return result
if __name__=="__main__":
    solution=Solution()
    nums=[1,2,3]
    result=solution.permute(nums)
    print(result)