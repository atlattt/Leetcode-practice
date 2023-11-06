class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = len(alphabet)
        result = ''
        while columnNumber > 0:
            columnNumber -= 1
            index = columnNumber % n
            result = alphabet[index] + result
            columnNumber //= n
        return result

if __name__=="__main__":
    solution=Solution()
    print(solution.convertToTitle(28))