import sys
a, b = map(int, input().split())
res = 0
while a:
    if a < b:
        a, b = b, a
    res += a // b
    a = a % b
print(res)