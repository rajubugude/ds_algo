#Easy

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))


def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(6))


# https://www.geeksforgeeks.org/sum-triangle-from-array/
def sum_traingle_arr(arr):
    if len(arr) < 1:
        return
    new = []
    for i in range(len(arr)-1):
        new.append(arr[i] + arr[i+1])
    
    sum_traingle_arr(new)
    print(arr)

arr = [1, 2, 3, 4, 5]
(sum_traingle_arr(arr))


#i assumed my arr elements are positive, max element is < 100
def maxi_mini(arr):
    if not arr:
        return float('-inf'), float('inf') #maxi, mini
    
    maxi, mini = maxi_mini(arr[1:])
    maxi = max(maxi, arr[0])
    mini = min(mini, arr[0])
    return maxi, mini # returns tuple 

print(maxi_mini(arr))
    

def binary_search(arr,n):
    pass