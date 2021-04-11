sum_cache = {0:0, 1:1}

def fibonacci(n):
    """Returns the fibonacci sum of a number n"""
    assert n >= 0, 'n must be >= 0'

    if n in sum_cache:
        return sum_cache[n]
    res = n + fibonacci(n-1) + fibonacci(n-2)
    sum_cache[n] = res
    return res

if __name__ == '__main__':
    from timeit import Timer 
    t = Timer('fibonacci(300)', 'from __main__ import fibonacci')
    print('Time: ', t.timeit())
