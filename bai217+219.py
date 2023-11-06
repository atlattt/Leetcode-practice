from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Array - Hashing: Set -> O(n)
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        else:
            return False
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp={}
        for i,num in enumerate(nums):
            if num in tmp and i-tmp[num]<=k:
                return True
            tmp[num]=i
        return False
                