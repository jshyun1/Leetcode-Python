import math
class Solution:
    def numTrees(self, n: int) -> int:
        return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
    
solution = Solution()
print(solution.numTrees(3))  # Output: 5
print(solution.numTrees(1))  # Output: 1
print(solution.numTrees(2))  # Output: 2
print(solution.numTrees(4))  # Output: 14
        