def sort(list1):
    i = 0
    list = []
    list1 = sorted(list1)
    for i in range(0,len(list1)-1):
        if list1[i] != list1[i+1]:
            list.append(list1[i])
        else:
            continue
        i += 1
    return list

list1 = [1, 3, 5, 7, 9,9,9,9,1,3]


print(sort(list1))