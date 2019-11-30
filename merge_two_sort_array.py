#!/usr/bin/env python
# coding:utf-8

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        知道两个数组原先的长度，就可以知道合并后的长度，
        
        倒叙遍历两个数组，大的数优先放到合并后的数组对应下标处。
        如果第一个数组先遍历完，那应该把第二个数组剩下的元素复制过来；
        如果第二个先遍历玩，就不用变化了，因为第一个数组剩余的元素已经在目标位置
        """
        index = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1
        if m < 0:
            nums1[:n + 1] = nums2[:n + 1]

def main():
    s = Solution()
    s.merge([1, 1, 2, 2, 4, 0, 0, 0, 0], 5, [0, 0, 2, 3], 4)

if __name__ == "__main__":
    main()
