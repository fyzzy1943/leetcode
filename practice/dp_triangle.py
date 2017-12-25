

n = int(input())
triangle = []
for _ in range(n):
    nums = input().split()
    tmp = []
    for num in nums:
        tmp.append(int(num))
    triangle.append(tmp)

def maxSum(i, j):
    if i == n:
        return triangle[i-1][j-1]

    x = maxSum(i+1, j)
    y = maxSum(i+1, j+1)
    return max(x, y) + triangle[i-1][j-1]

print(triangle)
print(maxSum(1, 1))
