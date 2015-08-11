#dp problem 

n, C = map(int, input().split())
V, W = [], []
for i in range(n):
    a, b = map(int, input().split())
    V.append(a)
    W.append(b)

d = [[0] * 100 for _ in range(100)]
#0,1 dp
for i in range(n + 1):
    for j in range(C + 1):
        d[i][j] = 0 if i == 0 else d[i - 1][j];
        if i > 0 and j > V[i - 1]:
            tmp = d[i - 1][j - V[i - 1]] + W[i - 1]
            if tmp > d[i][j]:
                d[i][j] = tmp

print(d[n][C])
'''test
for i in range(n + 1):
    for j in range(C + 1):
        print(d[i][j], end = ' ')
    print()
'''