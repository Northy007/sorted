def bubleSorted(l) :
    n = len(l) - 1
    swapStack = 0
    for i in range(n + 1):
        for j in range(0, n-i):
            if l[j] > l[j + 1] :
                l[j], l[j + 1] = l[j + 1], l[j]
                swapStack += 1
    return swapStack


inp = [int(x) for x in input("Enter Input : ").split()]
if bubleSorted(inp) != 0 :
    print("No")
else :
    print("Yes")

