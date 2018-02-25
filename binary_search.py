def binary_search(alist, target, start, end):
    if start < end:
        mid = (start + end) // 2
        if alist[mid] == target:
            return mid
        elif alist[mid] < target:
            return binary_search(alist, target, mid + 1, end)
        elif alist[mid] > target:
            return binary_search(alist, target, start, mid - 1)
    return None

print(binary_search([2, 3, 4, 3], 3, 0, 3))
