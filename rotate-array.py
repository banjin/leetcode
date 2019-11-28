#!/usr/bin/env python3
# coding:utf-8

class Solutions:
    def rotate_array(self, nums, k):
        """
        """
        import copy
        nums_b = copy.deepcopy(nums)
        length = len(nums)
        for i, v in enumerate(nums):
            nums_b[(i+k)%length] = v
        for i,v  in enumerate(nums_b):
            nums[i] = nums_b[i]
        print(nums)
    
    def rotate_arry2(self, nums, k):
        """参考leetcode 解题
        """
        length = len(nums)
        k %= length
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)
    
    def rotate_array3(self, nums, k):
        """
        如此简单，但是我没想出来
        """
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]
        print(nums)
    
    def rotate_array4(self, nums, k):
        """插入
        """
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())
        print(nums)



def main():
    s = Solutions()
    s.rotate_array4([1,2,3,4,5,6,7], 3)
    


if __name__ == "__main__":
    main()

