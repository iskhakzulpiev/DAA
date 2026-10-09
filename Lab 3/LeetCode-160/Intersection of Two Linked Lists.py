class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        while pA != pB:
            pA = pB if pA is None else pA.next
            pB = headA if pB is None else pB.next
            
        return pA