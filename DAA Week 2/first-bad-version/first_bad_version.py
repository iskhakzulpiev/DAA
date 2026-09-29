def firstBadVersion(n: int) -> int:
    low = 1
    high = n
    ans = n
    while low <= high:
        mid = (low + high) // 2

        if firstBadVersion(mid):
            ans = mid       
            high = mid - 1
        else:
            low = mid + 1

    return ans