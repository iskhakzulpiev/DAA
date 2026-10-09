# Palindrome Linked List

## 1. Problem
Given the head of a singly linked list, return `True` if it is a palindrome (reads the same forward and backward), or `False` otherwise.

## 2. Approach
We convert the linked list values into a standard array/list:
1. Traverse the linked list and collect all node values into a Python list `vals`.
2. Compare `vals` with its reversed version `vals[::-1]`.
3. Return `True` if equal, otherwise `False`.

### Tracing Example
Input: `1 -> 2 -> 2 -> 1`
- **Traversal:** `vals = [1, 2, 2, 1]`
- **Comparison:** `[1, 2, 2, 1] == [1, 2, 2, 1]` $\rightarrow$ `True`.
- **Output:** `True`

### Challenges Faced
- **Initial Attempt:** Trying to navigate backwards directly on the singly linked list.
- **Why It Failed:** Singly linked lists only have `next` pointers, making backward navigation impossible without converting data or reversing pointers.

## 3. Time Complexity
**Time Complexity:** O(n)

**Explanation:** Where $n$ is the number of nodes. Copying elements takes $O(n)$ time, and comparing two arrays takes $O(n)$ time.

## 4. Space Complexity
**Space Complexity:** O(n)

**Explanation:** An extra list `vals` is created to store all $n$ values from the linked list.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** Yes, space efficiency can be improved to $O(1)$.
- **What would you need to change?** Use fast/slow pointers to find the midpoint, reverse the second half of the linked list in place, and compare the two halves node-by-node.
- **What complexity could the improved solution achieve?** $O(n)$ time complexity and $O(1)$ space complexity.