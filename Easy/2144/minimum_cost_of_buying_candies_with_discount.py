def minimumCost(cost):
    cost.sort(reverse=True)
    total_cost = 0

    for i in range(len(cost)):
        if (i + 1) % 3 != 0:
            total_cost += cost[i]

    return total_cost

# Example usage:
cost = [1, 2, 3]   
print(minimumCost(cost))  # Output: 5

cost = [6, 5, 7, 9, 2, 2]
print(minimumCost(cost))  # Output: 23
cost = [5, 5]
print(minimumCost(cost))  # Output: 10
cost = [1, 2, 3, 4, 5, 6]
print(minimumCost(cost))  # Output: 16
cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(minimumCost(cost))  # Output: 33