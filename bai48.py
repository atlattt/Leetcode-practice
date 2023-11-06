from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s.rotate(matrix)
for row in matrix:
    print(row)