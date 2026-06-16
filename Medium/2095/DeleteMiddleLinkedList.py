# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 노드가 1개뿐인 경우 중간 노드를 삭제하면 빈 리스트가 됨
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None  # 느린 포인터의 이전 노드를 가리킬 포인터
        
        # fast는 2칸씩, slow는 1칸씩 이동
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # slow가 중간 노드를 가리키고 있을 때, 이전 노드의 next를 다다음 노드로 연결
        prev.next = slow.next
        
        return head
solution = Solution()
# 예시: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = solution.deleteMiddle(head)
# 결과: 1 -> 2 -> 4 -> 5
current = new_head
while current:
    print(current.val, end=' -> ' if current.next else '')
    current = current.next
    
