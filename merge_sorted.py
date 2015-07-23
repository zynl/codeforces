# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#merge_sort to solve problem
def equal(a, b):
    def msort(s):
        length = len(s)
        if length % 2:
            return s
        s1 = msort(s[:length // 2])
        s2 = msort(s[length // 2:])
        if s1 < s2:
            return s1 + s2
        else:
            return s2 + s1
    if msort(a) == msort(b):
        return True
    else:
        return False
a = input()
b = input()

print('YES' if equal(a, b) else 'NO')