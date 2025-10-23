#Easy

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(4))


# def fib(n):
#     if n < 2: return n
#     return fib(n-1) + fib(n-2)

# print(fib(6))


# https://www.geeksforgeeks.org/sum-triangle-from-array/
# def sum_traingle_arr(arr):
#     if len(arr) < 1:
#         return
#     new = []
#     for i in range(len(arr)-1):
#         new.append(arr[i] + arr[i+1])
#
#     sum_traingle_arr(new)
#     print(arr)

# arr = [1, 2, 3, 4, 5]
# (sum_traingle_arr(arr))


#i assumed my arr elements are positive, max element is < 100
# def maxi_mini(arr):
#     if not arr:
#         return float('-inf'), float('inf') #maxi, mini
#
#     maxi, mini = maxi_mini(arr[1:])
#     maxi = max(maxi, arr[0])
#     mini = min(mini, arr[0])
#     return maxi, mini # returns tuple

# print(maxi_mini(arr))
    

# def reverseNum(n): #1234 -> 4321
#     if n <= 0:
#         return 0

#     rem = n % 10
#     small = reverseNum(n//10) #we assume for 123 it gives 321.
#     if small != 0:
#         count  = len(str(small))
#         digits = 10**(count)
#         rem = rem * digits
#     return rem + small

# print(reverseNum(1000))
    

# def reverseNum(n, ans): #1234 -> 4321
#     if n <= 0:
#         return ans

#     rem = n % 10
#     ans *= 10
#     ans += rem
#     return reverseNum(n//10, ans)


# print(reverseNum(1000, 0))



# def countZeros(n, c):
#     if n==0:
#         return c

#     rem = n % 10
#     if rem == 0:
#         c += 1
    
#     return countZeros(n//10, c)

# print(countZeros(102020, 0))


# def binary_search(arr,n):
#     pass


## Medium problems

#TODO IMP
#give list of all indices of target, don't use global list and don't pass list as argument.

#method 1
# def search_target(arr, target, idx):
#     ans = []
#     if idx == len(arr):
#         return ans
#     if target == arr[idx]:
#         ans.append(idx)
#     ans_below = search_target(arr, target, idx+1)
#     ans.extend(ans_below)
#     return ans


#method 2

# def search_target(arr, target, idx):
#     if idx == len(arr):
#         return []
    
#     current = [] 
#     if arr[idx] == target:
#         current.append(idx)
#     return current + search_target(arr, target, idx + 1)


# arr = [1,2,3,5,6,3,8,3]
# target = 3
# idx = 0
# print(search_target(arr, target, idx))


# def remove_a(s):
#     if not s:
#         return ''

#     small_ans = remove_a(s[1:])
#     if s[0] == 'a':
#         return small_ans
#     else:
#         return s[0]+small_ans

# s = 'bacad'
# print(id(s))
# ans = remove_a(s)
# print(id(ans))
# print(ans)


# count of even numbers in arr, using recursion,
#TODO: directly recursion fn should return the result.
#pattern : https://leetcode.com/problems/unique-paths-iii/, https://leetcode.com/problems/n-queens-ii/,
# def count_even(arr, i):
#     if i == len(arr):
#         return 0
#
#     count = 1 if arr[i] % 2 == 0 else 0
#     count += count_even(arr, i+1)
#     return count
#
# arr = [1, 2, 3, 5, 6, 7]
# print(count_even(arr, 0))  # Output: 2
#
#
# def count_even_backtrack(arr, i, count):
#     if i == len(arr):
#         return count  # Base case: return the accumulated count
#
#     res = 0
#
#     # Option 1: Count this element if it's even
#     if arr[i] % 2 == 0:
#         res += count_even_backtrack(arr, i + 1, count + 1)
#     else:
#         # Option 2: Skip counting this element
#         res += count_even_backtrack(arr, i + 1, count)
#
#     return res
#
# # Example usage
# arr = [1, 2, 3, 5, 6, 7]
# print(count_even_backtrack(arr, 0, 0))  # Output: 2

print('tejas_enb_shell'.title())
