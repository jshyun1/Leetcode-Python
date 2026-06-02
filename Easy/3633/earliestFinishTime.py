from typing import List


def earliestFinishTime(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int: 
    minFinishTime = 300000
    for i in range(len(landStartTime)):
        landFinishTime = landStartTime[i] + landDuration[i]
        
        for j in range(len(waterStartTime)):
            waterFinishTime = waterStartTime[j] + waterDuration[j]
            
            if landFinishTime <= waterStartTime[j] or waterFinishTime <= landStartTime[i]:
                FinishTime = max(landFinishTime, waterFinishTime)
            else:
                FinishTime = max(landFinishTime + waterDuration[j], waterFinishTime + landDuration[i]) 
            minFinishTime = min(minFinishTime, FinishTime)   
    
    return minFinishTime



print(earliestFinishTime([1, 2, 3], [3, 2, 1], [4, 5, 6], [1, 2, 3]))  
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [2, 3, 4], [1, 2, 3]))  
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 2, 3])) 
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [5, 6, 7], [1, 2, 3])) 
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [6, 7, 8], [1, 2, 3])) 
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [7, 8, 9], [1, 2, 3])) 
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [8, 9, 10], [1, 2, 3]))  
print(earliestFinishTime([1, 2, 3], [3, 2, 1], [9, 10, 11], [1, 2, 3]))  