def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = []
        while head:
            data.append(head.val)
            head = head.next
        if data == data[::-1]:
            return True
          
 def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find the middle   
        slow, fast = ListNode(0, head), head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first, second, slow.next = head, slow.next, None
        
        # 2. reverse second half
        prev = None
        while second:
            second.next, prev, second, = prev, second, second.next
        second = prev
        
        # 3. compare
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        return True
