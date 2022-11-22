def bubleSorted(l,n,m) :
    if l ==  [] :
        return []
    if m == len(l) - 1 :
        return l
    if n == len(l) - 1 :
        return bubleSorted(l,0,m + 1)
    else :
        if l[n] > l[n + 1] :
            l[n], l[n + 1] = l[n + 1], l[n]
        return bubleSorted(l, n + 1,m)

print(bubleSorted([8,2,5,3,1,4],0,0))