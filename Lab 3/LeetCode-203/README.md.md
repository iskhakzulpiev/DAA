# Remove Linked List Elements

## 1. Problem
Given the head of a linked list and an integer `val`, remove all nodes from the linked list that have `ListNode.val == val`, and return the new head.

## 2. Approach
We use a dummy node to handle edge cases where the target value is at the head:
1. Create a `dummy` node pointing to `head` and place `current` at `dummy`.
2. Inspect `current.next`.
3. If `current.next.val == val`, remove it by setting `current.next = current.next.next`.
4. Otherwise, move `current` forward.

### Tracing Example
Input: `1 -> 2 -> 6 -> 3`, `val = 6`
- **Start:** `dummy(0) -> 1 -> 2 -> 6 -> 3`, `current` at `dummy`
- **Step 1:** `current.next.val` is 1 $\neq 6 \rightarrow$ advance `current` to 1.
- **Step 2:** `current.next.val` is 2 $\neq 6 \rightarrow$ advance `current` to 2.
- **Step 3:** `current.next.val` is 6 $= 6 \rightarrow$ set `current.next` to 3. (List becomes `0 -> 1 -> 2 -> 3`).
- **Step 4:** `current.next.val` is 3 $\neq 6 \rightarrow$ advance `current` to 3.
- **End:** `current.next` is `None`. Return `dummy.next` (`1`).

### Challenges Faced
- **Initial Attempt:** Traversing directly without a dummy node.
- **Why It Failed:** Removing the head node (or multiple leading nodes matching `val`) required extra `if` checks and special logic, causing `AttributeError` on empty lists.

## 3. Time Complexity
**Time Complexity:** O(n)

**Explanation:** Where $n$ is the number of nodes in the list. Each node is inspected exactly once.

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** We modify node pointers in place using a single dummy node and pointer, using constant extra memory.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** No, $O(n)$ time and $O(1)$ space are optimal.
- **What would you need to change?** Recursion can be used: `head.next = removeElements(head.next, val)`.
- **What complexity could the improved solution achieve?** Recursive solution takes $O(n)$ time and $O(n)$ stack space.