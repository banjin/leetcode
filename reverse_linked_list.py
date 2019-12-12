#!/usr/bin/env python
#coding:utf-8

"""
单列表翻转
"""

class Solution:

    def reverseList(self,head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
