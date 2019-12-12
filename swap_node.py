#!/usr/bin/env python
#coding:utf-8

"""
翻转相邻两个元素
"""

class Solution:
    def swapPairs(self, head):
        pre , pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
