def IntoAlphabet(s):
    x = ""
    for i in s :
        if i.isalpha():
            x = i
            break
    return x

def bubleSorted(l) :
    n = len(l) - 1
    swapStack = 0
    for i in range(n + 1):
        for j in range(0, n-i):
            if ord(IntoAlphabet(l[j])) > ord(IntoAlphabet(l[j + 1])) :
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


inp = input("Enter Input : ").split()
print(" ".join(bubleSorted(inp)))

