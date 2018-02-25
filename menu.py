def duplicate(a_list):
    n = []
    for i in range(1, len(a_list)):
        k = i - 1
        count = 1
        while k >= 0 and count <= 2:
            if a_list[i] == a_list[k]:
                count += 1
            k -= 1
        if count >= 2:
            if a_list[i] not in n:
                n.append(a_list[i])
    return n


print(duplicate([1, 2, 3, 3, 5, 6, 7, 7, 7, 7]))
