# Linked List Cycle

## 1. Problem
We are given the head of a linked list. We need to determine if the list contains a cycle (a loop where following `next` pointers keeps going infinitely).

## 2. Approach
We use Floyd's Cycle-Finding Algorithm (Fast & Slow pointers):
1. Initialize two pointers, `slow` and `fast`, at the head of the list.
2. Move `slow` forward by 1 node at a time.
3. Move `fast` forward by 2 nodes at a time.
4. If there is a cycle, `fast` will eventually catch up to `slow` from behind inside the loop.
5. If `fast` reaches `None`, the list has an end, so no cycle exists.

### Tracing Example
Input list: `1 -> 2 -> 3 -> 4 -> (points back to 2)`

- **Start:** `slow` at `1`, `fast` at `1`
- **Iteration 1:** `slow` goes to `2`, `fast` goes to `3`
- **Iteration 2:** `slow` goes to `3`, `fast` goes to `2` (following loop from `4` back to `2`)
- **Iteration 3:** `slow` goes to `4`, `fast` goes to `4`
- **Check:** `slow == fast` (`4 == 4`). Cycle found! Return `True`.

## 3. Time Complexity
**Time Complexity:** O(n)

**Explanation:** Where $n$ is the total number of nodes in the linked list. If there is no cycle, `fast` reaches the end in $n / 2$ steps. If there is a cycle, `fast` will catch up to `slow` in at most $n$ iterations inside the loop.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** The algorithm only uses two pointer variables (`slow` and `fast`), taking constant extra space regardless of list size.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(n)$ time and $O(1)$ space are optimal.
- **What would you need to change?** An alternative approach is to use a Hash Set to store visited node references and check if a node repeats.
- **What complexity could the improved solution achieve?** A Hash Set approach also achieves $O(n)$ time, but it increases space complexity to $O(n)$ to store all nodes. Thus, the two-pointer approach remains the most memory-efficient choice.