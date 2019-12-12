#!/usr/bin/env python
# coding:utf8

"""
探测环,判断链表中是否有环
"""

def hasCycle(self, head):
    fast = slow = head
    while slow and fast and fast.next:
        show = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
        return False
