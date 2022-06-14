def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            nextPtr = curr.next
            curr.next = pre
            pre = curr
            curr = nextPtr
        return pre
