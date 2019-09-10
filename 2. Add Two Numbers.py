# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        current = None
        carry = False
        while (l1 is not None or l2 is not None or carry is True):
            x1 = l1.val if l1 is not None else 0
            x2 = l2.val if l2 is not None else 0
            sum = x1 + x2 + (1 if carry else 0)

            if sum >= 10:
                carry = True
                sum -= 10
            else:
                carry = False

            if current is None:
                current = ListNode(sum)
                res = current
            else:
                current.next = ListNode(sum)
                current = current.next
            # print(display(res))
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return res


def display(x: ListNode):
    i = 1
    res = 0

    while (x is not None):
        res += x.val * (i if x.val != 0 else (i if i > 0 else 0))
        i *= 10
        x = x.next
    return res


x1 = ListNode(3)
x1.next = ListNode(4)
print(display(x1))

x2 = ListNode(8)
x2.next = ListNode(5)

r1 = Solution().addTwoNumbers(x1, x2)

# display(x1)
print(display(r1))
