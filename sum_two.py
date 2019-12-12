#!/usr/bin/env python3
#coding:utf-8


class Solution:
    def twoSum(self, nums, target):
        """使用字典
        """
        if not nums:
            return []
        temp_dict = dict()
        for i, v in enumerate(nums):
            if target - v in temp_dict:
                temp_dict[target-v] = nums.index(target-v)
                return [i, temp_dict[target-v]]
            else:
                temp_dict[v] = i

    def twoSum2(self, nums, target):
        nums2 = nums
        for i, v in enumerate(nums):
            for j, v_2 in enumerate(nums2[i+1:], start=i+1):
                if v + v_2 == target:
                    return [i, j]
        
        


def main():
    s = Solution()
    r = s.twoSum2([2,11,15, 7], 9)
    print(r)

if __name__ == "__main__":
    main()