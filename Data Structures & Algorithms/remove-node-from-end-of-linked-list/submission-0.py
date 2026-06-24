# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init = ListNode(0, head)
        left = init
        right = head

        #我们需要两个指针之间空出n个单位，这样子等right都到末尾的none的时候，left的右边就刚好是我们需要删除的指针了
        while n>0 :
            right = right.next
            n -= 1
        
        while right:
            left=left.next
            right = right.next
        
        #删除 需要删除的节点
        left.next = left.next.next

        return init.next
    





        