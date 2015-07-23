#quick_sort O(nlogn) worst n*n


A = list(map(int, input().split()))

def quick_sort(A, q, r):
    if q < r:
        p = partiton(A, q, r)
        quick_sort(A, q, p - 1)
        quick_sort(A, p + 1, r)

def partiton(A, q, r):
    x = r
    i = q
    for j in range(q, r + 1):
        if A[j] < A[x]:
            #print(A[i], A[j])
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[x] = A[x], A[i]
    return i

quick_sort(A, 0, len(A) - 1)
print(A)
    
    