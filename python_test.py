#collections, Counter, counter.most_common, enumerate, *(i, j) --> i, j
#float('inf')
#http://codeforces.com/contest/558/problem/B
import collections

n = int(input())
As = list(map(int, input().split()))

def solve(n, As):
    counter = collections.Counter(As)
    #print(counter)
    candidates = []
    prev_freq = 0
    #find numbers list that have most times  
    for num, freq in counter.most_common():
        if prev_freq and prev_freq != freq:
            break
        candidates.append(num)
        prev_freq = freq
    #build a list for each number in candidates
    lr = {cand:[] for cand in candidates}
    #find position for number in lr
    for i, a in enumerate(As, 1):
        if a in lr:
            lr[a].append(i)
    minspan = float('inf')
    for pos in lr.values():
        if pos[-1] - pos[0] < minspan:
            minspan = pos[-1] - pos[0]
            LR = (pos[0], pos[-1])
    return LR
     
print(*solve(n, As))