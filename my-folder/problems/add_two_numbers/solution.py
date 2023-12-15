# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry_over = 0
        i = 0
        while(l1 is not None or l2 is not None):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            if (i != 0):
                current.next= ListNode()
                current= current.next
            current.val = x + y + carry_over
            carry_over = current.val // 10
            current.val = current.val % 10
            i += 1
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if (carry_over > 0):
            current.next = ListNode()
            current = current.next
            current.val = current.val + carry_over
        return head
        

        