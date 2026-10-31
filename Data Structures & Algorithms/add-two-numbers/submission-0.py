# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:  #iterate till bigger node ends , you will replace remaining digits with 0 in smaller node while doing sum. if final carry is pending then that also needs to be added to node like in e.g 9 + 9
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y #reverse helps coz addition starts rom units place
            carry = sum // 10 #quotient
            digit = sum % 10 #remainder
            node = ListNode(digit)
            curr.next = node
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  