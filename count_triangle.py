#灵活清新的头脑

def tri(s):
    return s * s
    
a, b, c, d, e, f = map(int, input().split())
print(tri(a + b + c) - tri(a) - tri(c) - tri(e))