# Remove Duplicates from Sorted List

## 1. Problem
Given the head of a sorted linked list, delete all duplicate nodes so that each element appears only once, returning the updated sorted list.

## 2. Approach
Since the list is already sorted, all identical elements are adjacent to each other:
1. Start at `head` with a pointer `current`.
2. Compare `current.val` with `current.next.val`.
3. If they are equal, change `current.next` to skip the duplicate node (`current.next = current.next.next`).
4. If they are different, advance `current` to `current.next`.

### Tracing Example
Input: `1 -> 1 -> 2`
- **Iteration 1:** `current.val` (1) equals `current.next.val` (1). Skip node: list becomes `1 -> 2`. Pointer remains at first `1`.
- **Iteration 2:** `current.val` (1) does not equal `current.next.val` (2). Advance `current` to `2`.
- **End:** `current.next` is `None`. Loop finishes.
- **Output:** `1 -> 2`

### Challenges Faced
- **Initial Attempt:** I initially tried advancing `current = current.next` in every iteration regardless of whether a duplicate was found.
- **Why It Failed:** Advancing after removing a duplicate caused the code to skip checking triple duplicates (e.g., `1 -> 1 -> 1`), leaving extra duplicate nodes behind.

## 3. Time Complexity
**Time Complexity:** O(n)

**Explanation:** Where $n$ is the number of nodes in the linked list. The algorithm visits each node at most once.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** The list is modified in place using a single pointer variable, using constant extra space.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(n)$ time and $O(1)$ space are optimal because every node must be inspected at least once.
- **What would you need to change?** A recursive approach could be used.
- **What complexity could the improved solution achieve?** Recursion would maintain $O(n)$ time but would increase space complexity to $O(n)$ due to call stack frames.