def cum_sum(n): 
    assert n >=0 and int(n) ==n, 'The argument must be a non-negative integer'
    if n in [0,1]:
        return n 
    else:
        return n + cum_sum(n-1)

print(cum_sum(-7))