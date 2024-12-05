class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        arr1 = [0]*l
        j = 0
        for i in range(l):
            if nums[i]==0:
                continue
            else:
                arr1[j] = nums[i]
                j+=1
        for i in range(l):
            nums[i] = arr1[i]