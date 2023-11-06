class Solution:
    def shortestPalindrome(self, s: str) -> str:
        p = s[::-1]
        add = ""
        n = len(s)
        for i in range (n):
            a = s[0:n-i]
            b = p[i:]
            if (a!=b):
                add+=a[-1]
            else:
                break
        return add+s
if __name__=="__main__":
    solution=Solution()
    s = "abcd"
    result=solution.shortestPalindrome(s)
    print(result)