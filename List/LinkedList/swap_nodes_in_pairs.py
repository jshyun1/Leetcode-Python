# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:  #(1->2->3->4)
            node = head.next    # node(2)
            node.next, head = head, node.next # head(2->1)
            node.next.next = self.swapPairs(head)
            return node
        return head




