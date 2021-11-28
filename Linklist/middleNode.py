def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next != None :
            if fast.next.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next
        return slow
