# class Animal:
#     def __init__(self, name1):
#         self.name1 = name1
#
#     def eat(self):
#         print("eating")
#
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def __init__(self, name, count):
#         self.count = count
#         super().__init__(name)
#
#     def sound(self):
#         print("bark")
#
#
# dog = Dog("asdf", 2)
# print(dog.name)
# dog.eat()
# dog.sound()



# def my_decorator(func):
#     def wrapper():
#         print("before call")
#         func()
#         print("after call")
#     return wrapper
#
# @my_decorator
# def greet():
#     print("hello")

#
# print(greet())


# list_of_strings = ["silent", "span", "meat", "pans", "listen", "team", "snap", "mate"]
#
# from collections import Counter, defaultdict
# def group_anagrams(arr):
#     n = len(arr)
#     map = defaultdict(list)
#     for word in arr:
#         freq = Counter(word)
#         # map[freq].append(word)
#         # map[tuple(sorted(freq.items()))].append(word)
#     ans = []
#     for key in map:
#         ans.append(map[key])
#     return ans
# print(group_anagrams(list_of_strings))
# #     # ["silent", "span", "meat", "pans", "listen", "team", "snap", "mate"]
#     ans = []
#     seen = set()
#     for i in range(n):
#         curr = []
#         word = arr[i]
#         word_freq = Counter()
#         if word not in seen:
#             curr.append(word)
#             seen.add(word)
#             word_freq = Counter(word)
#         for j in range(i+1, n):
#             next_word = arr[j]
#             next_word_freq = Counter(next_word)
#             if word_freq == next_word_freq:
#                 curr.append(next_word)
#                 seen.add(next_word)
#         if curr:
#             ans.append(curr)
#     return ans

# print(group_anagrams(list_of_strings))




# def valid_parenthesis(s):
#     stack = []
#      for i in s:
#         if i == '(' or i == '[' or  i == '{':
#             stack.append(i)
#         else:
#             if not stack:
#                 return False
#             else:
#                 top = stack.pop()
#                 if i == ']' and top != '[':
#                     return False
#                 if i == '}' and top != '{':
#                     return False
#                 if i == ')' and top != '(':
#                     return False
#     return True if not stack else False
#
# string1 = "()[{}]"
# string2 = "([)]"
# print(valid_parenthesis(string1))
# print(valid_parenthesis(string2))


# # # Optimized

# def valid_parenthesis(s):
#     stack = []
#     bracket_map = {'(': ')', '[': ']', '{': '}'}
#     open_set = set(bracket_map.keys())
#     close_set = set(bracket_map.values())
#
#     for char in s:
#         if char in open_set:
#             stack.append(char)
#         elif char in close_set:
#             if not stack or bracket_map[stack.pop()] != char:
#                 return False
#     return not stack


'''
SQL 
actual question: have two tables one is employee table and other is salary table.
emplyoee table 
    -id
    -emplyoee name

salary table
    -id
    -emplyoee id
    -amount

✅ Common SQL Queries You Might Want:
1. Get all employees with their salaries:

SELECT e.id, e.employee_name, s.amount
FROM employee e
JOIN salary s ON e.id = s.employee_id;

2. Get the 4th highest salary (with employee details).
-- Step 1: Get the 4th highest distinct salary
SELECT e.id, e.employee_name, s.amount
FROM employee e
JOIN salary s ON e.id = s.employee_id
WHERE s.amount = (
    SELECT DISTINCT amount
    FROM salary
    ORDER BY amount DESC
    LIMIT 1 OFFSET 3
);

2. Get the 4th highest salary (with employee details) using DENSE_RANK().

SELECT e.id, e.employee_name, s.amount
FROM (
    SELECT employee_id, amount,
           DENSE_RANK() OVER (ORDER BY amount DESC) AS rnk
    FROM salary
) AS ranked_salaries
JOIN employee e ON e.id = ranked_salaries.employee_id
WHERE rnk = 4;

3. Get the highest salary per employee (if multiple entries exist):

SELECT e.id, e.employee_name, MAX(s.amount) AS highest_salary
FROM employee e
JOIN salary s ON e.id = s.employee_id
GROUP BY e.id, e.employee_name;


IF all in same table.

4th highest salary

SELECT DISTINCT amount
FROM salary
ORDER BY amount DESC
LIMIT 1 OFFSET 3;

all emplyoees with 4th highest salary.
-- Step 1: Get the 4th highest distinct salary
WITH FourthHighest AS (
    SELECT DISTINCT amount
FROM salary
ORDER BY amount DESC
LIMIT 1 OFFSET 3;
)

-- Step 2: Get all employees with that salary
SELECT *
FROM employees
WHERE salary = (SELECT salary FROM FourthHighest);
'''