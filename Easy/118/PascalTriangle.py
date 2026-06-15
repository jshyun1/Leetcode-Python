class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        for i in range(numRows):
            if i == 0:
                res = [[1]]
            else:
                res.append([1] + [res[i - 1][j - 1] + res[i - 1][j] for j in range(1, i)] + [1])
                
        return res
solution = Solution()
print(solution.generate(5))
