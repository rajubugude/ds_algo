# def helper(s):
#     print(id(s), 'id of arg')
#     # res = s[::-1]
#     res = 0
#     while s:
#         res *= 10
#         res += s % 10
#         s = s//10
        
#     print(id(res), 'id after res')
#     return res

# def reverse_str():
#     # s = 'abc'
#     # s = ['a','b','c']
#     s = 1234
#     print(s)
#     print(id(s), 'id of s')
#     ans = helper(s)
#     print(id(ans), 'id of ans')
#     print(ans)
#     return ans

# print(reverse_str())


# def helper(s, ans):
#     print(s, ans,'here 1')
#     ans = s[::-1]
#     print(s, ans,'here 2')
    

# def reverse_str():
#     s = ''
#     helper('abc', s)
#     return s

# print(reverse_str())


# from abc import ABC,abstractmethod
# class Reverse:
#     @abstractmethod
#     def reverse_logic():
#         '''Should be implemented in child'''

# class Reverse_String(Reverse):
#     def reverse_logic(st):
#         return st[::-1]

# class Reverse_Array(Reverse):
#     def reverse_logic(arr):
#         return arr[::-1]

# class ReverseDigit(Reverse):
#     @staticmethod
#     def reverse_logic(num: int) -> int:
#         reversed_num = int(str(num)[::-1])
#         return reversed_num


# from functools import singledispatch

# @singledispatch
# def reverse(data):
#     raise TypeError(f"Unsupported type: {type(data)}")

# @reverse.register
# def _(st: str) -> str:
#     return st[::-1]

# @reverse.register
# def _(arr: list) -> list:
#     return arr[::-1]

# @reverse.register
# def _(num: int) -> int:
#     return int(str(num)[::-1])


# from functools import singledispatchmethod

# class Reverser:
#     @singledispatchmethod
#     def reverse(self, data):
#         raise TypeError(f"Unsupported type: {type(data)}")

#     @reverse.register
#     def _(self, st: str) -> str:
#         return st[::-1]

#     @reverse.register
#     def _(self, arr: list) -> list:
#         return arr[::-1]

#     @reverse.register
#     def _(self, num: int) -> int:
#         return int(str(num)[::-1])


# 2nd maxi
# 3rd maxi
