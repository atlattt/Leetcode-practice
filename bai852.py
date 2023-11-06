
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
            return arr.index(max(arr))
if __name__=="__main__":
    solution=Solution()
    arr=[0,1,0]
    result=solution.peakIndexInMountainArray(arr)
    print(result)