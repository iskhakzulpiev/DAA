# Merge Two Sorted Lists

## 1. Problem
We are given the heads of two sorted linked lists. We need to merge them into a single sorted linked list by linking the existing nodes together and return the head of the new list.

## 2. Approach
We use an iterative approach with a dummy node:
1. Create a `dummy` node to anchor the result list and a `current` pointer to build it.
2. Compare the values at `list1` and `list2`.
3. Link `current.next` to the smaller node, then advance that list's pointer.
4. Move `current` forward.
5. Once one list becomes empty, attach the remaining nodes from the non-empty list.

### Tracing Example
Input: `list1 = [1, 3]`, `list2 = [2, 4]`

- **Initial:** `dummy = 0`, `current = dummy`
- **Iteration 1:** Compare `1` vs `2`. Since $1 \le 2$, set `current.next = 1`. Move `list1` to `3`.
- **Iteration 2:** Compare `3` vs `2`. Since $2 < 3$, set `current.next = 2`. Move `list2` to `4`.
- **Iteration 3:** Compare `3` vs `4`. Since $3 \le 4$, set `current.next = 3`. Move `list1` to `None`.
- **After Loop:** `list1` is empty. Attach remaining `list2` starting at `4`.
- **Final Result:** `1 -> 2 -> 3 -> 4`

## 3. Time Complexity
**Time Complexity:** O(n + m)

**Explanation:** Where $n$ and $m$ are the lengths of `list1` and `list2`. In each step of the loop, we process exactly one node. We visit each node from both lists at most once.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** We reuse the original nodes of the input lists by changing their `next` pointers. No new list nodes are created except for a single dummy pointer variable.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(n + m)$ time is optimal because every node must be inspected at least once to ensure correct sorted order.
- **What would you need to change?** We could write a recursive solution instead of an iterative loop.
- **What complexity could the improved solution achieve?** A recursive solution would still run in $O(n + m)$ time, but it would use $O(n + m)$ extra memory space on the call stack, making the iterative approach better for memory.