# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, tail, ptr , ptr1= 1, head, head, head
        while tail.next:
            tail = tail.next
            length += 1
        
        for i in range(n):
            ptr = ptr.next
        
        if not ptr:
            return ptr1.next
        
        curr = head
        for i in range(length - n -1):
            curr = curr.next
        curr.next = curr.next.next
        
        return head
        
