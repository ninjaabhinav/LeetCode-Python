class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_sort = sorted(nums)
        l=len(nums)
        for i in range(l-1):
            if nums_sort[i]==nums_sort[i+1]:
                return True
            # if nums_sort[i]!=nums_sort[i+1]:
        return False
                
