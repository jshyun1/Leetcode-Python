class Solution:
    def isPalindrome(self, x: int) -> bool:
        Num = str(x)
        ReverseNum = Solution.reverse(Num)
        return Num == ReverseNum

    def reverse(text):
        result = ""
        for i in text:
            result = i + result
        return result



