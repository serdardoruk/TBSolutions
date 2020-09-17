prices = [1,2,3]
# prices = [2,3,4,3,2,1]
# prices = [3,2,2,1]


def stockRuns(prices):
    longestTrend = 1
    maxLen = 0
    increasing = prices[1] > prices[0]
    for i in range(1, len(prices)):
        if increasing:
            if prices[i] > prices[i - 1]:
                longestTrend += 1
                maxLen = max(maxLen, longestTrend)
            else:
                longestTrend = 2
                increasing = False
        
        else:
            if prices[i] < prices[i - 1]:
                longestTrend += 1
                maxLen = max(maxLen, longestTrend)
            else:
                longestTrend = 2
                increasing = True

    return maxLen

print(stockRuns(prices))