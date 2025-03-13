from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        # neg = self.bs(nums, n, 0)
        
        # print(neg)
        pos = n - self.bs(nums, n, 1)
        print(pos)
    
    def bs(self, nums, n, target):
        start = 0
        end = n-1
        flag = False
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                flag = True
                end = mid - 1
            else:
                start = mid + 1
        return start if flag else -1
    
# arr = [-2, -1, 0, 0, 0, 1]
# arr = [-1, 0, 0, 1]
arr =[1,2,3,3]
# arr =[0,2,3,3]
s = Solution()
(s.maximumCount(arr))