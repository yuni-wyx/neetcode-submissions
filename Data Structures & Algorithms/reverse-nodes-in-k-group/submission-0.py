# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Initialize the kth node
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            for i in range(k):
                if kth is None:
                    break
                kth = kth.next

            if kth is None:
                break
            
            groupNext = kth.next
        
            # Reverse the K nodes

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = prev
            groupPrev = temp

        return dummy.next





        


