#Easy

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(4))


def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

# print(fib(6))


# https://www.geeksforgeeks.org/sum-triangle-from-array/
def sum_traingle_arr(arr):
    if len(arr) < 1:
        return
    new = []
    for i in range(len(arr)-1):
        new.append(arr[i] + arr[i+1])
    
    sum_traingle_arr(new)
    print(arr)

# arr = [1, 2, 3, 4, 5]
# (sum_traingle_arr(arr))


#i assumed my arr elements are positive, max element is < 100
def maxi_mini(arr):
    if not arr:
        return float('-inf'), float('inf') #maxi, mini
    
    maxi, mini = maxi_mini(arr[1:])
    maxi = max(maxi, arr[0])
    mini = min(mini, arr[0])
    return maxi, mini # returns tuple 

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

#TODO IMP
#give list of all indices of target, don't use global list and don't pass list as argument.

# def search_target(arr, target, idx):
#     ans = []
#     if idx == len(arr):
#         return ans
#     if target == arr[idx]:
#         ans.append(idx)
#     ans_below = search_target(arr, target, idx+1)
#     ans.extend(ans_below)
#     return ans


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

# n = 5
# for i in range(n+1):
#     for j in range(i):
#         print('*', end=' ')
#     print()


s = 'hit'
for i in range(len(s)):
    for j in range(26):
        char = chr(97+j)
        new = s[:i] + char + s[i+1:]
        print(new)



