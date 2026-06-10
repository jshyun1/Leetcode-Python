class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        num1_str = str(num1)
        num2_str = str(num2)
        length1 = len(str(num1_str))
        length2 = len(str(num2_str))
        waves = 0
        for num in range(num1, num2+1):
            num_str = str(num)
            length = len(num_str)
            for i in range(0, length):
                if i == 0 or i == length-1:
                    continue
                if num_str[i] > num_str[i-1] and num_str[i] > num_str[i+1]:
                    waves += 1
                elif num_str[i] < num_str[i-1] and num_str[i] < num_str[i+1]:
                    waves += 1
        return waves

# Example usage:
solution = Solution()
print(solution.totalWaviness(120, 130))  # Output: 2
print(solution.totalWaviness(10, 20))   # Output: 0
print(solution.totalWaviness(198, 202)) # Output: 1
print(solution.totalWaviness(1, 10))    # Output: 0






'''
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waves = 0
        
        for num in range(num1, num2 + 1):
            num_str = str(num)
            length = len(num_str)
            
            # 자릿수가 3개 미만이면 waviness가 존재할 수 없음
            if length < 3:
                continue
                
            # 0번과 length-1번 인덱스는 어차피 패스하므로 range 범위를 조절
            for i in range(1, length - 1):
                # 피크(Peak)이거나 밸리(Valley)인 경우를 한 줄로 깔끔하게 처리
                if (num_str[i] > num_str[i-1] and num_str[i] > num_str[i+1]) or \
                   (num_str[i] < num_str[i-1] and num_str[i] < num_str[i+1]):
                    waves += 1
                    
        return waves
        '''