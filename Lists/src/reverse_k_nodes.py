from typing import Optional

from src import ListNode


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]: # type: ignore
        
        group = 0
        cur = head

        while cur and group < k:
            cur = cur.next
            group += 1

        
        if group == k:
            cur = reverseKGroup(cur, k)

            while group > 0:
                tmp = head.next
                
                head.next = cur
                cur = head 
                head = tmp
                group -= 1

            head = cur
        return head