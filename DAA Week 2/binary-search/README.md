# Binary Search

## 1. Problem
Given a sorted integer array `nums` and a target integer `target`, return the index of `target` if it exists in the array. Otherwise, return `-1`.

## 2. Approach
We use two pointers, `low` and `high`, to track the current search range. In each iteration, we calculate the middle index `mid`:
- If `nums[mid] == target`, we return `mid`.
- If `nums[mid] < target`, the target lies in the right half, so we update `low = mid + 1`.
- If `nums[mid] > target`, the target lies in the left half, so we update `high = mid - 1`.
If `low > high` and the element is not found, we return `-1`.

## 3. Time Complexity
**Time Complexity:** O(log n)

**Explanation:** In each step, the algorithm eliminates half of the remaining elements. Halving an array of size n repeatedly reduces the search space to 1 element in at most O(log n) steps.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** The algorithm only uses a constant amount of memory for three boundary variables (`low`, `high`, `mid`).