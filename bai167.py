from typing import List
#CACH NAY TIME LIMIT EXCEEDED
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            result=[]
            n=len(numbers)
            i=0
            while(i<n):
                j=i+1
                while(j<n):
                    if(numbers[i]+numbers[j]==target):
                        result.append(i+1)
                        result.append(j+1)
                        return result
                    j=j+1
                i=i+1
#CACH TOI UU 
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        
        while numbers[i] + numbers[j]!=target:
            s = numbers[i] + numbers[j]        
            if s > target:
                j-=1
            else:
               i+=1 
        
        return [i + 1 , j + 1]
if __name__=="__main__":
    solution=Solution()
    solution1=Solution1()

    numbers = [2,7,11,15] 
    target = 9
    result=solution.twoSum(numbers,target)
    result1=solution.twoSum(numbers,target)
    print(result,result1)
                    
                        