from typing import List
# https://leetcode.com/contest/weekly-contest-448/problems/fill-a-special-grid/?slug=merge-operations-for-minimum-travel-time&region=global_v2
# def specialGrid(n: int):
#     if n == 0:
#         return [[0]]
#
#     # prev = specialGrid(n - 1)
#     prev = [[3,0],[2,1]]
#     size = len(prev)
#     new_size = size * 2
#     grid = [[0] * new_size for _ in range(new_size)]
#     offset = size * size
#     for i in range(size):
#         for j in range(size):
#             grid[i][j] = prev[i][j] + 3 * offset      # Top-left (A)
#             grid[i][j + size] = prev[i][j]            # Top-right (B)
#             grid[i + size][j + size] = prev[i][j] + offset  # Bottom-right (C)
#             grid[i + size][j] = prev[i][j] + 2 * offset      # Bottom-left (D)
#     return grid
#
#
# print(specialGrid(2))

# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
# import heapq
# class Solution:
#     def cal_sum(self, n):
#         ans = 0
#         while n:
#             ans += (n%10)
#             n = n//10
#         return ans
#
#     def minSwaps(self, nums: List[int]) -> int:
#         n = len(nums)
#         pq = []
#         for i, val in enumerate(nums):
#             summ = self.cal_sum(val)
#             heapq.heappush(pq, (summ, val))
#
#         ans = []
#         while pq:
#             _, val = heapq.heappop(pq)
#             ans.append(val)
#         # print(ans)
#
#         index_map = {val: i for i, val in enumerate(nums)}
#         swaps = 0
#
#         for i in range(n):
#             while nums[i] != ans[i]:
#                 swaps += 1
#                 swap_with = index_map[ans[i]]
#                 index_map[nums[i]] = swap_with
#                 nums[i], nums[swap_with] = nums[swap_with], nums[i]
#
#         return swaps

# s = Solution()
# nums = [18,43,34,16]
# print(s.minSwaps(nums))


# def minSwaps(arr):
#     # sorted_arr = arr.sort()
#     ele_idx_map = {val:i for i, val in enumerate(arr)}
#     print(ele_idx_map)
#
# arr = [3,1,2,5]
# print(minSwaps(arr))

#
# class Solution:
#     def is_consecutive(self, a, b):
#         if a == 'a' and b == 'z' or a == 'z' and b == 'a':
#             return True
#
#         val1 = ord(a)
#         val2 = ord(b)
#         return abs(val1-val2) == 1
#
#     def resultingString(self, s: str) -> str:
#         i = 1
#         while i < len(s):
#             # print(s[i])
#             if self.is_consecutive(s[i-1], s[i]):
#                 s = s[:i-1] + s[i+1:]
#                 i -= 2
#             i += 1
#         return s
#
# st = "saz"
# s = Solution()
# print(s.resultingString(st))

# class Solution:
#     def helper(self, nums, n):
#         count = 0
#         for i in range(n-1):
#             if nums[i] != nums[i+1]:
#                 nums[i] *= -1
#                 nums[i+1] *= -1
#                 count += 1
#         return count
#
#     def canMakeEqual(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         count = self.helper(nums, n)
#         print(nums)
#         start = nums[0]
#         for i in nums:
#             if i != start:
#                 return False
#         if count > k:
#             return False
#         return True
#
#
# nums = [-1,-1,-1,1,1,1]
# k = 5
# s = Solution()
# print(s.canMakeEqual(nums, k))


# https://leetcode.com/problems/inverse-coin-change/
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        arr = []
        for i in range(n):
            amount = i+1
            ways = numWays[i]
            if self.helper(len(arr), arr, amount, ways) == 0:
                return []
        return arr

    def helper(self, n, arr, amount, ways):
        if n == 0:
            if amount and ways:
                arr.append(amount)
                print(arr)
            # print(arr, 'here2')
        else:
            uniqueways = self.combinationSum(arr, amount)
            if uniqueways +1 < ways:
                return 0
            elif uniqueways+1 == ways:
                arr.append(amount)


    def combinationSum(self, candidates, target):
        n = len(candidates)
        return self.helper1(candidates, target, n, 0)


    def helper1(self, nums, target, n, idx):
        if idx == n:
            if target == 0:
                return 1
            return 0
        if target < 0:
            return 0

        one = self.helper1(nums, target-nums[idx], n, idx)
        two = self.helper1(nums, target, n, idx+1)
        return one + two


numWays = [0,1,0,2,0,3,0,4,0,5]
s = Solution()
print(s.findCoins(numWays))