#!/usr/bin/env python3

"""
二分查找
列表必须是有序列表，否则不能使用二分查找
将指定元素插入到列表中，且不改变原先的顺序
"""

class Solution:
    def search_insert(self, l, a):
        s = 0
        length = len(l)
        while s < length:
            mid = (s + length) // 2
            if l[mid] > a:
                length = mid
            else:
                s = mid + 1
        l.insert(s, a)

if __name__ == "__main__":
    d = [1,2,3,4,5,6,7,8,20,23,24,25,26]
    a = 3
    s = Solution()
    s.search_insert(d,a)
    print(d)
