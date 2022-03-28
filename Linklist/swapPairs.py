def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr, prev = head, dummy
        
        while curr and curr.next:
            nextpair = curr.next.next
            sndnode = curr.next
            
            sndnode.next = curr
            curr.next = nextpair
            prev.next = sndnode
            
            prev = curr
            curr = nextpair
            
        return dummy.next
