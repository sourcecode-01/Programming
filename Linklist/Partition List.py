class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1=ListNode(0)
        d2=ListNode(0)
        ls1,ls2=d1,d2
        while head:
            if head.val < x:
                ls1.next=head
                ls1=ls1.next
            else:
                ls2.next=head
                ls2=ls2.next
            head=head.next
        ls1.next=d2.next
        ls2.next=None
        return d1.next
