n, k = map(int, input().split())
buy = list(map(int, input().split()))
sell = list(map(int, input().split()))

dp = [[0 for j in range(k+1)] for i in range(n)]

#dp[i][j] i= index of num in buy list
# j = sell[i]

# if (sell[0]  -  buy[0] > 0):
#     dp[0][sell[0]] = sell[0] - buy[0]
for j in range(k + 1):
    if j >= buy[0]:
        dp[0][j] = max(dp[0][j], sell[0] - buy[0])

for i in range(1, n):
    for j in range(k+1):
        # skip
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        #take
        if j >= buy[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - buy[i]] + sell[i] - buy[i])

        # if j + sell[i] <= k and sell[i] >= buy[i]:
        #     dp[i][j + buy[i]] =  max(dp[i][j+buy[i]], dp[i-1][j] + sell[i] - buy[i])
# maxi = 0
# for j in range(k+1):
#     maxi = max(maxi, dp[n-1][j])
print(max(dp[n-1]))


# n, k= map(int, input().split())
# buy = list(map(int, input().split()))
# sell = list(map(int, input().split()))
# profit = [0]
# def findd(buy, sell, i, remaining):
#     if i < n and remaining <= k:
#         #take
#         # subset.append(sell[i] - buy[i])
#         if sell[i] - buy[i] > 0:
#             profit.append(sell[i] -  buy[i] + profit[-1])
#             findd(buy, sell, i+1, remaining - buy[i])
#         profit.pop()
#         findd(buy, sell, i+ 1,  remaining)
        
#     else:
#         return
# findd(buy, sell, 0, k)
# # print(max(list(profit)))
# print(max(profit)) 