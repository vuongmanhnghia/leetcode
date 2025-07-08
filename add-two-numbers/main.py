from types import ClassMethodDescriptorType
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        divisible = 0

        while l1 or l2 or divisible:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            value = v1 + v2 + divisible
            divisible = value // 10
            value = value % 10

            cur.next = ListNode(value)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


def create_nodelist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


list_1 = [int(x) for x in input("Press list_1... : ").split()]
list_2 = [int(x) for x in input("Press list_2... : ").split()]

l1 = create_nodelist(list_1)
l2 = create_nodelist(list_2)

solution = Solution()
solution.addTwoNumbers(l1, l2)
