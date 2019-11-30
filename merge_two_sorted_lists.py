#!/usr/bin/env python3
# coding:utf-8


class Solution:
    def merge_two_list(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.val < list2.val:
            list1.next = self.merge_two_list(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_two_list(list1, list2.next)
            return list2
