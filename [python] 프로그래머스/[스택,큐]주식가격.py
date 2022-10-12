def solution(prices):
    answer = []
    
    prices.append(0)
    for i in range(len(prices)):
        now = prices[i]
        for j in range(i+1, len(prices)):
            if prices[j] < now:
                if j == len(prices) - 1:
                    answer.append(j-i-1)
                    break
                else:
                    answer.append(j-i)
                    break
    
    return answer