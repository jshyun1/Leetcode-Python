
import re
class Solution:
    def processStr(self, s: str) -> str:
        stack = []
        for c in s:
            clean_chr = re.sub(r'[^a-zA-Z0-9\s]', '', c)
            if clean_chr:
                stack.append(clean_chr)
            elif c == '*':
                if stack:
                    stack.pop()
            elif c == '#':
                stack1 = stack
                stack.extend(stack1)# Remove the last character without popping
            elif c == '%':
                stack.reverse()                
        return ''.join(stack)
    
# Example usage:
solution = Solution()
print(solution.processStr("a#b%*"))


'''모범답안
class Solution:
    def processStr(self, s: str) -> str:
        ans = ""

        for x in s:
            if x == '*':
                ans = ans[:-1]

            elif x == '#':
                ans += ans

            elif x == '%':
                ans = ans[::-1]

            else:
                ans +=x

        return ans
'''