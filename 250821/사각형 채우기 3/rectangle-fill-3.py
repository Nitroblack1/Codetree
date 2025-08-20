n = int(input())

# Please write your code here.
dp = [0] * (n+1)

if n >= 1:
    dp[1] = 2
if n >= 2:
    dp[2] = 7

if n >= 3:
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2] * 3 + 2*(i-2)) % 1000000007

print(dp[n])