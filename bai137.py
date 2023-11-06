from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 3
        return nums[-1]
if __name__=="__main__":
    solution=Solution()
    a=[0,1,0,1,0,1,99]
    print(solution.singleNumber(a))