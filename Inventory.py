#http://codeforces.com/contest/569/problem/B

from collections import Counter

n = int(input())
A = list(map(int, input().split()))

def change_number():             #numbers needed
    set_list = set(A)
    for i in range(1, n + 1):
        if i not in set_list:
            yield i
            
C = Counter(A)        
it = change_number()
for i in range(n):
    if C[A[i]] > 1:
        C[A[i]] -= 1
        A[i] = next(it)
    elif A[i] > n:
        A[i] = next(it)

print(' '.join(A))