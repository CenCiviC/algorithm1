import sys
arr = [40, 20, 30, 10, 30]
n = len(arr)

dp = [[-1 for _ in range(n)] for _ in range(n)]

def matrixChainMemoised(p, i, j):
	if(i == j):
		return 0
	
	if(dp[i][j] != -1):
		return dp[i][j]
	
	dp[i][j] = sys.maxsize
	
	for k in range(i,j):
		dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
	return dp[i][j]

def MatrixChainOrder(p,n):
	i = 1
	j = n - 1
	return matrixChainMemoised(p, i, j)

print(MatrixChainOrder(arr, n))

