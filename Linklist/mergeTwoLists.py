def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currfirst = list1
        currSec = list2
        mergelist = dummy = ListNode(0)
        while True:
            if currfirst is None:
                mergelist.next = currSec
                break
            elif currSec is None:
                mergelist.next = currfirst
                break 
            elif currfirst.val <= currSec.val:
                mergelist.next = currfirst
                currfirst = currfirst.next
            else:
                mergelist.next = currSec
                currSec = currSec.next
            mergelist = mergelist.next
        return dummy.next
