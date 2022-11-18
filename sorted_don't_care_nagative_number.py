def SelectionSorted(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1,len(l)):
            if l[min_idx] >= 0 and l[j] >= 0 :
                if l[min_idx] > l[j] :
                    min_idx = j

        l[i], l[min_idx] = l[min_idx], l[i]



inp = [int(x) for x in input("Enter Input : ").split()]
SelectionSorted(inp)
for char in inp :
    print(char, end = " ")