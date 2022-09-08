def prod_list(lst):
    if len(lst)==0:
        return 0
    if len(lst)==1:
        return lst[0]
    else:
        return lst[len(lst)-1] * prod_list(lst[:len(lst)-1])

print(prod_list([1,2,3,4,5]))