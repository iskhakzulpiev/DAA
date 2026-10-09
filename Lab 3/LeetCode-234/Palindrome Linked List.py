class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current = head
        
        while current:
            vals.append(current.val)
            current = current.next
            
        return vals == vals[::-1]