T = int(input())
a = int(input())
sum = 0
for arr in range(1,T): # arr:0~T-1
    arr = arr*10
for i in range(T):
    gv = a%10
    arr = arr//10
    sum = sum + (a%arr)
print(sum)


