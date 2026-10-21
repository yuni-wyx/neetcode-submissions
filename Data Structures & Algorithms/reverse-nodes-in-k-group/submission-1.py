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
            # 1. 找到這一組最後一個 Node
            kth = groupPrev

            for i in range(k):
                if kth is None:
                    break
                kth = kth.next

            if kth is None:
                break
            
            # 2. 記住下一組的起點
            groupNext = kth.next
        
            # Reverse the K nodes
            # 3. 反轉這 k 個 Nodes
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Reconnect the nodes
            # 4. 把反轉後的這一組接回去
            temp = groupPrev.next
            groupPrev.next = prev

            # 5. 移動到這一組的尾端
            groupPrev = temp

        return dummy.next





        


