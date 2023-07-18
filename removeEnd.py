#TC - O(len of list)
#SC - O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy 
        fast = head
        for i in range(n):
            if fast==None:
                return
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next 
        slow.next = slow.next.next
        return dummy.next
        