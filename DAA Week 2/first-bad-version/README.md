# First Bad Version

## 1. Problem
Given $n$ product versions numbered $1$ to $n$, where all versions after a bad version are also bad, find the index of the first bad version while minimizing calls to `isBadVersion(version)`.

## 2. Approach
We apply binary search across the range of versions from `low = 1` to `high = n`:
- Calculate the middle version `mid`.
- Call `isBadVersion(mid)`:
  - If `True`, `mid` is bad, but an earlier version might also be bad. We record `mid` as a candidate answer and search the left half (`high = mid - 1`).
  - If `False`, all versions up to `mid` are good, so we search the right half (`low = mid + 1`).
We return the recorded answer when `low > high`.

## 3. Time Complexity
**Time Complexity:** O(log n)

**Explanation:** Each API check halves the remaining search space of versions. Reducing $n$ versions by half each iteration requires at most O(log n) API calls.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** The algorithm only uses a few variables (`low`, `high`, `mid`, `ans`) to manage the state, requiring constant extra memory.