#!/usr/bin/env python3

class Solutions:
    def remove_duplication(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        k = 1 #用于记录前一元素
        while(k < len(nums)):
            if nums[k] == nums[k-1]:
                del nums[k]
            else:
                k += 1
        return k


def main():
    s = Solutions()
    result = s.remove_duplication([1,1,2])
    print(result)

if __name__ == "__main__":
    main()
