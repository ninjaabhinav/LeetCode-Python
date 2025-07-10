class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        arr = []
        for i in s:
            if i in arr:
                while i in arr:
                    arr.pop(0)
            arr.append(i)
            count = max(count,len(arr))
        return count