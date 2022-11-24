# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next=None
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tt = tt2 = ListNode(None)
        while list1 and list2:
            if list1.val < list2.val:
                tt.next = list1
                list1 = list1.next
            else:
                tt.next = list2
                list2 = list2.next
            tt = tt.next
        tt.next = list1 or list2
        return tt2.next
            
        
        
        