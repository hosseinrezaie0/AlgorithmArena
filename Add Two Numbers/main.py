class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add(l1, l2):
    val = l1.val + l2.val
    res = ListNode(val % 10)
    carry = val // 10
    temp = res
    l1, l2 = l1.next, l2.next
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = v1 + v2 + carry
        temp.next = ListNode(val % 10)
        temp = temp.next
        carry = val // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return res
