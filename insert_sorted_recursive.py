def insertSorted(l,arr,i):
    if l != [] :
        if arr == []:
            arr.append(l.pop(0))
        if l[0] < arr[i]:
            x = l.pop(0)
            arr.insert(i,x)
            if l != [] :
                print("insert {0} at index {1} : {2} {3}".format(x,i,arr,l))
            else :
                print("insert {0} at index {1} : {2}".format(x,i,arr))
            return insertSorted(l,arr,0)
        elif i == len(arr) - 1 :
            x = l.pop(0)
            arr.append(x)
            if l != [] :
                print("insert {0} at index {1} : {2} {3}".format(x,i + 1,arr,l))
            else :
                print("insert {0} at index {1} : {2}".format(x,i + 1,arr))
            return insertSorted(l,arr,0)
        return insertSorted(l,arr,i + 1)
    print("sorted")
    print(arr)

inp = [int(x) for x in input("Enter Input : ").split()]
insertSorted(inp,[],0)