# # from abc import ABC, abstractmethod
# #
# # class Exam:
# #     var_one = 1
# #     _var_two = 2
# #     __var_three = 3
# #
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def public_method(self):
# #         print("Do something in public")
# #         print(f"can access public var: {Exam.var_one}")
# #
# #     def _protected_method(self):
# #         print("Do something in protected")
# #         print(f"can access protected var: {Exam._var_two}")
# #
# #     @classmethod
# #     def class_method(cls):
# #         return f"can access all {cls.var_one} {cls._var_two} {cls.__var_three}"
# #
# #     def describe(self):
# #         print(f"Describing exam object: {self.name}")
# #
#
# # obj = Exam("Jee")
# # obj.describe()
# # print(obj.class_method())
# # obj._protected_method()
# # obj.public_method()
# # print(Exam.class_method())
#
#
# # def reverse_words_in_sentence(string):
# #     print(len(string))
# #     l = string.split(" ")
# #     print(l)
# #     new_l =l[::-1]
# #     res = " ".join(new_l)
# #     print(len(res))
# #     return res
# #
# # string = "hello my Name is Raju"
# # res = reverse_words_in_sentence(string)
# # print(res)
#
#
# # map = {}
# # freq = {'a':1, "c":3, 'b':2, 'd':1}
# # print(freq.items())
# # print(sorted(freq.items()))
# # print(tuple(sorted(freq.items())))
# # map[tuple(sorted(freq.items()))] = 1
# # print(map)
# import threading
#
# class Singleton:
#     _instance = None
#     _lock = threading.Lock()
#     @staticmethod
#     def get_instance():
#         if Singleton._instance is None:
#             with Singleton._lock:
#                 if Singleton._instance is None:
#                     print("Creating new instance")
#                     Singleton._instance = Singleton()
#                     return Singleton._instance
#         print("Using existing instance")
#         return Singleton._instance
#
# class SingleTon:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print("Creating new instance")
#             cls._instance = super().__new__(cls)
#         else:
#             print("Using existing instance")
#         return cls._instance
#
# # Usage
# s1 = SingleTon()
# s2 = SingleTon()
# s3 = Singleton.get_instance()
# s4 = Singleton.get_instance()
#
# print(s1 is s2)  # True — both are the same instance
# print(s3 is s4)  # True — both are the same instance

# import asyncio
# import time
#
# async def hello1():
#     await asyncio.sleep(5)
#     print("hello1 print")
#
# async def hello2():
#     await asyncio.sleep(5)
#     print("hello2 print")
#
# async def main():
#     task1 = asyncio.create_task(hello1())
#     task2 = asyncio.create_task(hello2())
#     await task1
#     await task2
#
# if __name__ == "__main__":
#     start_time = time.time()
#     asyncio.run(main())
#     print("Total time:", time.time() - start_time)


# arr = [1,2,3,4]
# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print(arr[j], end=' ')
#     print()

# class Solution:
#     def isPossible(self, n, arr):
#         third = float('-inf')
#         stack = []
#
#         # Traverse from right to left
#         for i in range(n - 1, -1, -1):
#             if arr[i] < third:
#                 return True
#
#             while stack and stack[-1] < arr[i]:
#                 third = max(third, stack.pop())
#
#             stack.append(arr[i])
#
#         return False
#
# s= Solution()
# # arr = [3, 1, 4, 2]
# arr = [1,2,3,4]
# print(s.isPossible(4, arr))

# nums = [2,4,5,6,8]
# for i in nums:
#     if i&1:
#         continue
#     print(i)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = [int(i) for i in input().split()]
#     st = set(arr)
#     length = len(st)
#     print((length*2)-1)

from collections import  defaultdict
from sys import flags


# # arr = [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
# arr = [0, 0, 0, 1, 1, 1]
# # ranges = [[1,12], [2,7], [5,10], [6,11]]
# ranges = [[1,3], [4,6], [1,6]]
# from collections import  defaultdict
#
# t = int(input())
# for _ in range(t):
#     n,q = [int(i) for i in input().split()]
#     arr = [int(i) for i in input().split()]
#     ranges = []
#     for _ in range(q):
#         s,e = [int(i) for i in input().split()]
#         ranges.append([s,e])
#
#     ans  = []
#     for l, r in ranges:
#         l = l-1
#         r = r-1
#         length = r-l+1
#         map_ind = defaultdict(list)
#         for i in range(l,r+1):
#             map_ind[arr[i]].append(i)
#         #freq check of 0's 1's equal or else all 0's or all 1's
#         keys = list(map_ind.keys())
#         key = keys[0]
#         values= map_ind[key]
#
#         if len(map_ind) == 1:
#             if length == len(values):
#                 ans.append(length//3)
#
#         else:
#             zero_indices = map_ind[0]
#             one_indices = map_ind[1]
#             if len(zero_indices) % 3 == 0 and len(one_indices) % 3 == 0:
#                 #if alternate = length//2
#                 diff = zero_indices[0]
#                 flag0 = True
#                 for i in zero_indices[1:]:
#                     diff += 2
#                     if diff != i:
#                         flag0 = False
#                         break
#
#                 diff = one_indices[0]
#                 flag1 = True
#                 for i in one_indices[1:]:
#                     diff += 2
#                     if diff != i:
#                         flag1 = False
#                         break
#
#                 if flag1 and flag0:
#                     ans.append(length//2)
#                 else:
#                     ans.append(length//3)
#                 #else:length//3
#             else:
#                 ans.append(-1)
#
#     for i in ans:
#         print(i)
#







# def is_alternating(subarr):
#     for i in range(1, len(subarr)):
#         if subarr[i] == subarr[i - 1]:
#             return False
#     return True
#
# t = int(input())
# for _ in range(t):
#     n, q = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     # Precompute prefix sums for 0s and 1s
#     prefix_0 = [0] * (n + 1)
#     prefix_1 = [0] * (n + 1)
#     for i in range(n):
#         prefix_0[i + 1] = prefix_0[i] + (1 if arr[i] == 0 else 0)
#         prefix_1[i + 1] = prefix_1[i] + (1 if arr[i] == 1 else 0)
#
#     ranges = [tuple(map(int, input().split())) for _ in range(q)]
#     ans = []
#
#     for l, r in ranges:
#         l -= 1
#         r -= 1
#         length = r - l + 1
#         subarr = arr[l:r + 1]
#         unique_vals = set(subarr)
#
#         if len(unique_vals) == 1:
#             ans.append(length // 3)
#         elif is_alternating(subarr):
#             ans.append(length // 2)
#         else:
#             count_0 = prefix_0[r + 1] - prefix_0[l]
#             count_1 = prefix_1[r + 1] - prefix_1[l]
#             if count_0 % 3 == 0 and count_1 % 3 == 0:
#                 ans.append(length // 3)
#             else:
#                 ans.append(-1)
#
#     print(ans)
#     print(prefix_0)
#     print(prefix_1)

# def solve():
#     N, Q = map(int, input().split())
#     A = [0] + list(map(int, input().split()))  # 1-based indexing
#
#     MAX = N + 2
#     sum_0 = [0] * MAX
#     sum_1 = [0] * MAX
#     diff = [0] * MAX
#     diffsum = [0] * MAX
#
#     for i in range(1, N + 1):
#         sum_0[i] = sum_0[i - 1]
#         sum_1[i] = sum_1[i - 1]
#         if A[i] == 0:
#             sum_0[i] += 1
#         else:
#             sum_1[i] += 1
#
#         diff[i] = int(A[i] != A[i - 1])
#         diffsum[i] = diffsum[i - 1] + diff[i]
#     # print(sum_0, '0sum')
#     # print(sum_1, '1sum')
#     # print(diffsum, 'diffsum')
#     # print(diff)
#     for _ in range(Q):
#         l, r = map(int, input().split())
#         z = sum_0[r] - sum_0[l - 1]
#         o = sum_1[r] - sum_1[l - 1]
#
#         if z % 3 != 0 or o % 3 != 0:
#             print(-1)
#             continue
#
#         result = z // 3 + o // 3
#         if diffsum[r] - diffsum[l] == (r - l):
#             result += 1
#         print(result)
#
#
# T = int(input())
# for _ in range(T):
#     solve()


#
# class Solution:
#     def minArrivalsToDiscard(self, nums, w: int, m: int) -> int:
#         freq = defaultdict(int)
#         n = len(nums)
#         count = 0
#         i = 0
#         j = 0
#         while j < n:
#             freq[nums[j]] += 1
#             while j - i + 1 > w:
#                 freq[nums[i]] -= 1
#                 if freq[nums[i]] == 0:
#                     del freq[nums[i]]
#
#                 i+= 1
#             if freq[nums[j]] > m:
#                 count += 1
#                 freq[nums[j]] -= 1
#                 nums[j] = 0
#             j += 1
#         return count
#
# nums = [7,7,7,7,7]
# m = 1
# w = 2
# s = Solution()
# print(s.minArrivalsToDiscard(nums,w,m))


# abc = [1,2,3]
# def fn(abc):
#     def1 = [6,7,8]
#     # abc += def1
#     # abc.extend(def1) #both are same
#     abc = abc + def1
#     print(abc, 'here')
#
# fn(abc)
# print(abc)



# def lower_bound(arr,target):
#     ans = ""
#     s = 0
#     e = len(arr)-1
#     while s <= e:
#         mid = (s+e)//2
#         if arr[mid] <= target:
#             ans = arr[mid]
#             s = mid+1
#         else:
#             e = mid-1
#     return ans
#
# arr = [1, 4, 7, 10]
# print(lower_bound(arr, 9))


# https://codeforces.com/contest/2160/problem/A
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = [int(i) for i in input().split()]
#     st =set(arr)
#     for i in range(102):
#         if i not in st:
#             print(i)
#             break


# https://codeforces.com/contest/2160/problem/B
# t = int(input())
# for _ in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     c=2
#     res=[1]
#     for i in range(1,n):
#         d=l[i]-l[i-1]
#         diff = i-d
#         if diff>=0:
#             res.append(res[diff])
#         else:
#             res.append(c)
#             c+=1
#     print(*res)


# from collections import defaultdict
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     freq = defaultdict(list)
#     for i,val in enumerate(s):
#         freq[val].append(i+1)
#
#     if len(freq) > 1:
#         print(len(freq['1']))
#         print(*freq['1'])
#     else:
#         print(0)


def solve(a, b):
    if a == b:
        return [0, []]

    x = a ^ b
    if x <= a:
        return [1, [x]]

    for bit in range(30):
        intermediate = a | ((1 << bit) - 1)
        if intermediate > a:
            x1 = a ^ intermediate
            if x1 <= a:
                x2 = intermediate ^ b
                if x2 <= intermediate:
                    return [2, [x1, x2]]
    return [-1, []]

t = int(input())
for _ in range(t):
    a,b = [int(i) for i in input().split()]
    ans = solve(a,b)
    if ans[0] != -1:
        print(ans[0])
        if ans[1]:
            print(*ans[1])
    else:
        print(-1)