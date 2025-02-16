def closest_binary_search(a, t):
    start = 0
    end = len(a) - 1
    result = 0
    while start <= end:
        # mid = start + (end - start) // 2
        mid = (start + end) // 2
        if a[mid] == t:
            return a[mid]
        if a[mid] < t:
            result = a[mid]
            start = mid + 1
        else:
            end = mid - 1
    return result


print(closest_binary_search([1, 3, 5, 7, 10, 16], 8))
