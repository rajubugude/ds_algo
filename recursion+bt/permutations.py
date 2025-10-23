# https://www.youtube.com/watch?v=T8hqjK94Fig&list=PLpIkg8OmuX-KJPC18SGiRUzJQAYo839ox&index=8

# Problem: https://leetcode.com/problems/permutations/description/

#appraoch 1: using set for checking at that curr recursion path(dfs) whether the ele is used or not,
#       coz we are traversing from idx 0 to n everytime.
# declaring as a class variable.

from typing import List
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         self.st = set()
#         self.helper(res, [], nums, n)
#         return res
#
#     def helper(self, res, temp, nums, n):
#         if len(temp) == n:
#             res.append(temp[:])
#             return
#
#         for idx in range(n):
#             if nums[idx] not in self.st:
#                 temp.append(nums[idx])
#                 self.st.add(nums[idx])
#                 self.helper(res, temp, nums, n)
#                 temp.pop()
#                 self.st.remove(nums[idx])
#


#approach 1. a): passing set as a parameter/argument.

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         self.helper(res, [], set(), nums)
#         return res
#
#     def helper(self, res, temp, used, nums):
#         if len(temp) == len(nums):
#             res.append(temp[:])
#             return
#
#         for idx in range(len(nums)):
#             if nums[idx] not in used:
#                 temp.append(nums[idx])
#                 used.add(nums[idx])
#                 self.helper(res, temp, used, nums)
#                 temp.pop()
#                 used.remove(nums[idx])


#approach 2: creating new list each time of recursion call, so that at end no need to copy current (temp) list.

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         self.st = set()
#         self.helper(res, [], nums, n)
#         return res
#
#     def helper(self, res, temp, nums, n):
#         if len(temp) == n:
#             res.append(temp)
#             return
#
#         for idx in range(n):
#             if nums[idx] not in self.st:
#                 self.st.add(nums[idx])
#                 self.helper(res, temp + [nums[idx]], nums, n)
#                 self.st.remove(nums[idx])
#

#appraoch 3: not using set, just swap and pass to recursion.

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         n = len(nums)
#         self.helper(ans, nums, 0, n)
#         return ans
#
#     def helper(self, ans, nums, idx, n):
#         if idx == n:
#             ans.append(nums[:])
#             return
#
#         for i in range(idx,n):
#             nums[idx], nums[i] = nums[i], nums[idx]
#             self.helper(ans, nums, idx+1, n)
#             nums[idx], nums[i] = nums[i], nums[idx]

# approach 4: assume your recursion gives you smaller permutations of length(nums)-1.
# for the smaller ones you insert the nth ele or array in all the positions.

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return self.helper(nums)
#
#     def helper(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 1:
#             return [nums[:]]  # Base case: return a list of one permutation
#
#         small = self.helper(nums[1:])  # Get permutations of the smaller list
#         permut = []
#
#         for perm in small:
#             for j in range(len(perm) + 1):
#                 permut.append(perm[:j] + [nums[0]] + perm[j:])
#
#         return permut


# Problem: https://leetcode.com/problems/permutations-ii/

from collections import Counter
#appraoch 1: use global freq for each ele, similar to set as used above.



#appraoch2: at each recursion call , before calling recusion,
# use set to choose which element to be swapped and avoid duplicate (so using set)

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         n = len(nums)
#         nums.sort()
#         self.helper(ans, nums, 0, n)
#         return ans
#
#     def helper(self, ans, nums, idx, n):
#         if idx == n:
#             ans.append(nums[:])
#             return
#
#         seen = set()
#         for i in range(idx,n):
#             if nums[i] in seen:
#                 continue
#             seen.add(nums[i])
#             nums[idx], nums[i] = nums[i], nums[idx]
#             self.helper(ans, nums, idx+1, n)
#             nums[idx], nums[i] = nums[i], nums[idx]
#
# s = Solution()
# s.permuteUnique([1,1,2])


# Problem: https://leetcode.com/problems/letter-tile-possibilities/description/

#TODO - no base case.
#appraoch 1:

# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         sequences = set()
#         used = [False] * len(tiles)
#
#         # Generate all possible sequences including empty string
#         self._generate_sequences(tiles, "", used, sequences)
#
#         # Subtract 1 to exclude empty string from count
#         return len(sequences) - 1
#
#     def _generate_sequences( self, tiles: str, current: str, used: list, sequences: set) -> None:
#        # here if we add only current whose length is len(tiles), then they are permutations 1 problem.
#         sequences.add(current)
#         # Try adding each unused character to current sequence
#         for pos, char in enumerate(tiles):
#             #here no need to pass index to recursion as we are always starting from start to end.
#             if not used[pos]:
#                 used[pos] = True
#                 self._generate_sequences(tiles, current + char, used, sequences)
#                 used[pos] = False


#approach 2:

# from collections import Counter
# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         charCount = Counter(tiles)
#         return self.count_possibilities(charCount)
#
#     def count_possibilities(self, charCount):
#         total_count = 0
#
#         for char in charCount:
#             if charCount[char] > 0:
#                 charCount[char] -= 1  # Temporarily decrement count
#                 total_count += 1
#                 total_count += self.count_possibilities(charCount)
#                 charCount[char] += 1  # Restore count for other branches
#
#         return total_count


#appraoch 3: subsets- II, permutaions -II mix.

# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         n = len(tiles)
#         curr = []
#         ans = []
#         tiles = list(tiles)
#         tiles.sort()
#         self.subseq_without_dup(curr, n, tiles, 0, ans)
#         res = 0
#         for word in ans:
#             count = self.permutations_without_dup(word, len(word), 0)
#             res += count
#         return res
#
#     def permutations_without_dup(self, s, n, idx):
#         if idx == n:
#             return 1
#
#         seen = set()
#         count = 0
#         for i in range(idx, n):
#             if s[i] in seen:
#                 continue
#             seen.add(s[i])
#             s[idx], s[i] = s[i], s[idx]
#             count += self.permutations_without_dup(s, n, idx+1)
#             s[idx], s[i] = s[i], s[idx]
#         return count
#
#     def subseq_without_dup(self, subset, n, s, i, res):
#         if i == n:
#             if subset:
#                 res.append(subset[:])
#             return
#
#         subset.append(s[i])
#         self.subseq_without_dup(subset, n, s, i+1, res) #include
#
#         subset.pop() #exclude, so remove
#         while i + 1 < len(s) and s[i] == s[i+1]:
#             i += 1
#         self.subseq_without_dup(subset, n, s, i+1, res) #exclude