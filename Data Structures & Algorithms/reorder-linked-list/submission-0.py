# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        #find median of LL
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
               
        # slow is the mid point
        curr = slow.next
        slow.next = None #break initial list 

        #reverse the list after the mid point
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #reorder now
        head2 = prev #head of reverse LL
        l1 = head
        l2 = head2
        while l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l2 = l2_next
            l1=l1_next

        return


        