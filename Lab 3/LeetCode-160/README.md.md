# Intersection of Two Linked Lists

## 1. Problem
Given the heads of two singly linked lists, return the node where the two lists intersect. If they do not intersect, return `None`.

## 2. Approach
We use a two-pointer technique:
1. Pointer `pA` starts at `headA`, and `pB` starts at `headB`.
2. Move both pointers forward one step at a time.
3. When `pA` reaches the end of List A, redirect it to `headB`. When `pB` reaches the end of List B, redirect it to `headA`.
4. If the lists intersect, both pointers travel equal total distance ($lenA + lenB$) and meet at the intersection node. If no intersection exists, both reach `None` at the same time.

### Tracing Example
List A: `1 -> 2 -> 3 -> 4`, List B: `9 -> 3 -> 4` (Intersect at `3`)
- **Step 1:** `pA` at 1, `pB` at 9
- **Step 2:** `pA` at 2, `pB` at 3
- **Step 3:** `pA` at 3, `pB` at 4
- **Step 4:** `pA` at 4, `pB` at `None` $\rightarrow$ redirect `pB` to `headA` (1)
- **Step 5:** `pA` reaches `None` $\rightarrow$ redirect `pA` to `headB` (9), `pB` moves to 2
- **Step 6:** `pA` moves to 3, `pB` moves to 3 (`pA == pB`)
- **Output:** Node `3`

### Challenges Faced
- **Initial Attempt:** Nested loops comparing every node in List A to every node in List B.
- **Why It Failed:** This brute-force approach resulted in $O(n \times m)$ time complexity, leading to a "Time Limit Exceeded" error on large inputs.

## 3. Time Complexity
**Time Complexity:** O(n + m)

**Explanation:** Where $n$ is the length of List A and $m$ is the length of List B. In the worst case, each pointer travels through both lists at most once ($n + m$ steps).

## 4. Space Complexity
**Space Complexity:** O(1)

**Explanation:** Only two pointer variables (`pA` and `pB`) are used, requiring constant extra space.

## 5. Reflection / Improvement
- **Is there a more efficient approach?** Time complexity $O(n + m)$ and space complexity $O(1)$ are already optimal.
- **What would you need to change?** A Hash Set could store all nodes of List A, then List B is scanned to find the first matching reference.
- **What complexity could the improved solution achieve?** That approach achieves $O(n + m)$ time but increases space complexity to $O(n)$.