#map/reduce, filter, sorted
#埃氏筛法

#create a iter 3, 5, 7, 9, 11, 13, ...
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0
    
def primes():
    yield 2
    it = _odd_iter() # initial iter
    while True:
        n = next(it) # return next number of iter 
        yield n
        it = filter(_not_divisible(n), it)
# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break