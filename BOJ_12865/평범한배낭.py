import sys; input = sys.stdin.readline
n, k = map(int, input().split())

bag_list= []
for _ in range(n):
    w, v = map(int, input().split())
    bag_list.append((w,v))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j < bag_list[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag_list[i-1][0]]+bag_list[i-1][1])

print(dp[n][k])