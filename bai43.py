class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
solution=Solution()
num1="123"
num2="456"
result=solution.multiply(num1,num2)
print(type(result))