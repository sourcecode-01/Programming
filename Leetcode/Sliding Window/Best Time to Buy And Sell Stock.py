# Input: prices = [7,1,5,3,6,4]
# Output: 5

prices = [7,1,5,3,6,4]

l, r = 0, 1
maxP = 0

while r < len(prices):
    if prices[l] < prices[r]:
        profit = prices[r] - prices[l]
        maxP = max(profit, maxP)
    else:
        l = r
        r += 1

print(maxP)
