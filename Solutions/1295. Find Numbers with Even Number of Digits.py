class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        def numOfDigit(n):
            count1 = 0
            while (n!=0):
                n=n//10
                count1+=1
            return count1
        for i in nums:
            ans = numOfDigit(i)
            if ans%2==0:
                count+=1
        return count