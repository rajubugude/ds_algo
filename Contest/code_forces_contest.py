# # https://codeforces.com/contest/2108/problem/A
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     maxi = 0
#     start = 1
#     curr = n
#     while curr:
#         maxi += abs(curr-start)
#         start += 1
#         curr -= 1
#
#     half = maxi//2
#     print(half+1)
#
from collections import Counter
from math import gcd
from sys import flags
from xml.dom.expatbuilder import theDOMImplementation

# https://codeforces.com/contest/2107/problem/A
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     l=list(map(int,input().split()))
#     m1=max(l)
#     m2=min(l)
#     if m1==m2:
#         print("NO")
#     else:
#         print("YES")
#         l2=[1 if i!=m1 else 2  for i in l]
#         print(*l2)

# def solve(arr, n):
#     maxi = max(arr)
#     mini = min(arr)
#     if maxi == mini:
#         return False, []
#     ans = []
#     for i in arr:
#         if i == maxi:
#             ans.append(2)
#         else:
#             ans.append(1)
#     return True, ans
#
#
#
# for _ in range(int(input())):
#     size = int(input())
#     arr = list(map(int, input().split()))
#     ans, res = solve(arr, size)
#     if ans:
#         print('yes')
#         for i in res:
#             print(i, end=' ')
#         print()
#     else:
#         print('no')


# * (iterable) is a shorthand in Python that unpacks the list l2 and prints its elements separated by spaces.
# print([1,2,1,1])
#
# print(*[1,1,2,1])
#
# t = (4, 5, 6)
# print(*t)  # ➜ 4 5 6
#
#
#
#
# s = "abc"
# print(*s)  # ➜ a b c
#
# s = {7, 8, 9}
# print(*s)  # ➜ 7 8 9 (order not guaranteed)
#
# print(*"hello", sep="-")  # ➜ h-e-l-l-o

# # https://codeforces.com/contest/2107/problem/B
# t = int(input())
# for i in range(t):
#     n, k = [int(i) for i in input().split()]
#     a = [int(i) for i in input().split()]
#     mx = max(a)
#     mn = min(a)
#     cnt = a.count(mx)
#     if mx - mn > k + 1 or (mx - mn == k + 1 and cnt > 1):
#         print("Jerry")
#     elif sum(a) % 2:
#         print("Tom")
#     else:
#         print("Jerry")


# # https://codeforces.com/problemset/problem/1890/A
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     freq = Counter(a)
#
#     if len(freq) >= 3:
#         print('No')
#     else:
#         values = list(freq.values())
#         if len(values) == 1 or abs(values[0] - values[1]) <= 1:
#             print('Yes')
#         else:
#             print('No')


# # https://codeforces.com/problemset/problem/1881/A

# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     x = input()
#     s = input()
#
#     if s in x:
#         print(0)
#         continue
#
#     ans = 0
#     original = x
#     while len(x) <= m+n:
#         x += original
#         original = x
#         ans += 1
#         if s in x:
#             print(ans)
#             break
#     else:
#         print(-1)

# def solve():
#     n, m = map(int, input().split())
#     x = input()
#     s = input()
#     for i in range(6):
#         if s in x:
#             print(i)
#             return
#         x += x
#     print(-1)
#
#
# for _ in range(int(input())):
#     solve()

# https://codeforces.com/contest/2102/problem/A
# t = int(input())
# for _ in range(t):
#     n, m, p, q = map(int, input().split())
#     if n%p == 0:
#         k = n//p
#         if k*q != m:
#             print('No')
#         else:
#             print('YES')
#     else:
#         print('YES')


# https://codeforces.com/contest/2107/problem/C
# t = int(input())
# for _ in range(t):
#     n, k= map(int, input().split())
#     s = input()
#     arr = list(map(int, input().split()))
#
#     summ = sum(arr)
#     count = 0
#     for i in range(n):
#         if s[i] == '0':
#             count += 1
#     if summ == k:
#         for i in range(n):
#             if s[i] == '0':
#                 arr[i] = 0
#         print('YES')
#         print(*arr)
#
#     elif summ > k:
#         rem = summ - k
#         if rem
#         val = rem // count
#         for i in range(n):
#             if s[i] == '0':
#                 arr[i] = val
#
#         print('NO')
#
#
#     else:
#         for i in range(n):
#             if s[i] == '0':
#                 arr[i] = k
#                 break
#         print('YES')
#         print(*arr)

# https://codeforces.com/contest/2102/problem/B

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     req = a[0]
#     a.sort()
#
#     ele = 0
#     pos = 0
#     if n%2 == 0:
#         pos = (n//2)-1
#         ele = a[pos]
#     else:
#         pos = n//2
#         ele = a[pos]
#
#     prev = a[pos-1]
#     after = a[pos+1]
#

# st = {1,2,3,3}
# print(list(st))

# https://codeforces.com/contest/2109/problem/0
# def solve(a, n):
#     if a[0] == a[1]:
#         print('YES')
#         return
#
#     for i in range(1,n-1):
#         if a[i] == 0 and a[i+1] == 0:
#             print('YES')
#             return
#
#     print('NO')
#     return
# def solve(a, n):
#     if sum(a) > n - 1:
#         print("YES")
#         return
#     for i in range(n - 1):
#         if a[i] == 0 and a[i + 1] == 0:
#             print("YES")
#             return
#     print("NO")
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     solve(a,n)

# https://codeforces.com/contest/2102/problem/B
# count of elements smaller than 0th idx ele, abs value of all <= n//2 to make median else not possible.
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     K = sum(1 for x in a[1:] if abs(x) < abs(a[0]))
#     if K <= n//2:
#         print("YES")
#     else:
#         print("NO")

# https://codeforces.com/problemset/problem/1873/C
# t = int(input())
# for _ in range(t):
#     grid = []
#     for _ in range(10):
#         chars_row = input().strip()
#         grid.append(chars_row)
#
#     ones = 0
#     twos = 0
#     threes = 0
#     fours = 0
#     fives = 0
#     for i in range(10):
#         for j in range(10):
#             if grid[i][j] == 'X':
#                 if i == 0 or i == 9 or j == 0 or j == 9:
#                     ones += 1
#                 elif i == 1 or i == 8 or j == 1 or j == 8:
#                     twos += 1
#
#                 elif i == 2 or i == 7 or j == 2 or j == 7:
#                     threes += 1
#
#                 elif i == 3 or i == 6 or j == 3 or j == 6:
#                     fours += 1
#
#                 elif i == 4 or i == 5 or j == 4 or j == 5:
#                     fives += 1
#
#     print(ones * 1 + threes * 3 +  fours * 4+ twos * 2 + fives * 5)


# https://codeforces.com/contest/2110/problem/A
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     mini = min(a)
#     maxi = max(a)
#
#     if (mini + maxi) % 2 == 0:
#         print(0)
#     else:
#         if mini % 2 == 0 and maxi % 2 != 0:
#             # make both even
#             a1 = a[:]
#             freq = Counter(a1)
#             make_even = 0
#             while True:
#                 if not a1:
#                     break
#                 maxi = max(a1)
#                 if maxi % 2 == 0:
#                     break
#                 make_even += freq[maxi]
#                 a1 = [x for x in a1 if x != maxi]
#                 freq = Counter(a1)
#
#             # make both odd
#             a2 = a[:]
#             freq = Counter(a2)
#             make_odd = 0
#             while True:
#                 if not a2:
#                     break
#                 mini = min(a2)
#                 if mini % 2 != 0:
#                     break
#                 make_odd += freq[mini]
#                 a2 = [x for x in a2 if x != mini]
#                 freq = Counter(a2)
#
#             print(min(make_even, make_odd))
#
#         elif mini % 2 != 0 and maxi % 2 == 0:
#             # make both even
#             a1 = a[:]
#             freq = Counter(a1)
#             make_even = 0
#             while True:
#                 if not a1:
#                     break
#                 mini = min(a1)
#                 if mini % 2 == 0:
#                     break
#                 make_even += freq[mini]
#                 a1 = [x for x in a1 if x != mini]
#                 freq = Counter(a1)
#
#             # make both odd
#             a2 = a[:]
#             freq = Counter(a2)
#             make_odd = 0
#             while True:
#                 if not a2:
#                     break
#                 maxi = max(a2)
#                 if maxi % 2 != 0:
#                     break
#                 make_odd += freq[maxi]
#                 a2 = [x for x in a2 if x != maxi]
#                 freq = Counter(a2)
#
#             print(min(make_even, make_odd))



# https://codeforces.com/contest/2110/problem/B
# t = int(input())
# for _ in range(t):
#     # s = '(()())' this case my logic is wrong.
#     s = input()
#     if ')(' in s:
#         print("YES")
#     else:
#         print("NO")

# t = int(input())
# for _ in range(t):
#     s = input()
#     close = False
#     ans = True
#     for i in s:
#         if i == ')':
#             close = True
#         if close and i == '(':
#             ans = False
#             break
#
#     if not ans:
#         print('YES')
#     else:
#         print('NO')

# t = int(input())
# for _ in range(t):
#     s = input()
# # (())
# # ()
# # (())(())
#
# # s = '(())()()'
# # s = '(())'
# # s = '(()())'
#     n = len(s)
#     bal = 0
#     ans = False
#     for i in range(n):
#         if s[i] == '(':
#             bal += 1
#         else:
#             bal -= 1
#         if i > 0 and i < n-1 and bal == 0:
#             ans = True
#     if ans:
#         print("YES")
#     else:
#         print("NO")


# https://codeforces.com/contest/2114/problem/A
# t = int(input())
# for _ in range(t):
#     s = input()
#     first = int(s[:2])
#     second = int(s[2:])
#     target = (int(s)**(0.5))
#     # print(target, 'target')
#     if (first+second) == target:
#         print(*[first, second])
#
#     elif not target %1 == 0:
#         print(-1)
#
#     else:
#         target = int(target)
#         print(*[1, target-1])


# https://codeforces.com/contest/2114/problem/B
# wrong ans
# t = int(input())
# for _ in range(t):
#     n, k = [int(i) for i in input().split()]
#     s = input()
#     ones = 0
#     zeroes = 0
#     count = 0
#     i = 0
#     j = len(s)-1
#     while i < j:
#         if s[i] == s[j]:
#             if s[i] == '1':
#                 ones += 1
#             else:
#                 zeroes += 1
#             count += 1
#         i += 1
#         j -= 1
#     if count == k:
#         print('YES')
#     elif abs(ones-zeroes) == k:
#         print('YES')
#     else:
#         print('NO')

#correct ans

# t = int(input())
# for _ in range(t):
#     n, k = [int(i) for i in input().split()]
#     s = input()
#     l = [1 for i in s if i == '0']
#     print(l)
#     zeroes = sum(l)
#     ones = n - zeroes
#     while k > 0:
#         if zeroes > ones:
#             zeroes -= 2
#         else:
#             ones -= 2
#         k -= 1
#     if ones == zeroes:
#         print('YES')
#     else:
#         print('NO')


# https://codeforces.com/contest/2114/problem/C
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     count = 1
#     last  = a[0]
#     for i in range(1,n):
#         if a[i]> 1 + last:
#             count += 1
#             last = a[i]
#     print(count)


# https://codeforces.com/contest/2116/problem/A
# t = int(input())
# for _ in range(t):
#     ga, fb, gk, fk = [int(i) for i in input().split()]
#     mini_g = min(ga, gk)
#     mini_f = min(fb, fk)
#     if mini_g >= mini_f:
#         print("Gellyfish")
#     else:
#         print("Flower")


# https://codeforces.com/contest/2116/problem/B
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     b = [int(i) for i in input().split()]
#     mod = 998244353
#     arr1 = [(2**i)%mod for i in a]
#     arr2 = [(2**i)%mod for i in b]
#     result = []
#
#     for i in range(n):
#         max_sum = 0
#         for j in range(i + 1):
#             max_sum = max(max_sum, (arr1[j] + arr2[i - j])%mod)
#         max_sum = max_sum%mod
#         result.append(max_sum)
#
#     print(*result)


# from typing import List
# from collections import deque
#
# class Solution:
#     def minMoves(self, grid: List[str], energy: int) -> int:
#         count = 0
#         m = len(grid)
#         n = len(grid[0])
#         r,c = -1, -1
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 'L':
#                     count += 1
#                 elif grid[i][j] == 'S':
#                     r,c = i, j
#
#         return self.bfs(r, c, grid, count, m, n, energy)
#
#     def bfs(self, r, c, grid, count, m, n, energy):
#         queue = deque()
#         directions = [0, 1, 0, -1, 0]
#         queue.append((r, c, 0, 0,  energy))
#
#         while queue:
#             x, y, moves, curr_count, curr_energy = queue.popleft()
#
#             if count == curr_count:
#                 return moves
#
#             for k in range(4):
#                 dx = x + directions[k]
#                 dy = y + directions[k + 1]
#
#                 if 0 <= dx < m and 0 <= dy < n:
#                     new_energy = curr_energy - 1
#                     if grid[dx][dy] == 'R':
#                         new_energy = energy
#                     elif grid[dx][dy] == 'L':
#                         curr_count += 1
#                     elif grid[dx][dy] == 'X':
#                         continue
#
#                     if new_energy >= 0:
#                         queue.append((dx, dy, moves + 1, curr_count, new_energy))
#
#         return -1
#
# s = Solution()
# grid = ["LS", "RL"]
# energy = 4
# print(s.minMoves(grid, energy))


# def print2X2(grid):
#     n = len(grid)
#     m = len(grid[0])
#     k = 2  # size of the subgrid
#
#     for i in range(n - k + 1):
#         for j in range(m - k + 1):
#             # Print the 2x2 subgrid starting at (i, j)
#             print(grid[i][j], grid[i][j+1])
#             print(grid[i+1][j], grid[i+1][j+1])
#             print()  # Blank line between subgrids
#
# grid = [[1, -2, 3],
#         [2,  3, 5]]
#
# print2X2(grid)
#
# def printKxK(grid, k):
#     n = len(grid)
#     m = len(grid[0])
#
#     if k > n or k > m:
#         print("Subgrid size is too large for the given grid.")
#         return
#
#     for i in range(n - k + 1):
#         for j in range(m - k + 1):
#             # Print the k x k subgrid starting at (i, j)
#             for x in range(k):
#                 for y in range(k):
#                     print(grid[i + x][j + y], end=' ')
#                 print()
#             print()  # Blank line between subgrids
#
# # Example usage:
# grid = [
#     [1, -2, 3],
#     [2,  3, 5],
#     [4,  6, 8]
# ]
#
# printKxK(grid, 2)

# from collections import deque
# n, m, k = map(int, input().split())
# maze = [list(input().strip()) for _ in range(n)]
# sx, sy, ex, ey = map(int, input().split())
#
# # Adjust for 0-based indexing
# sx -= 1
# sy -= 1
# ex -= 1
# ey -= 1
#
# direc = [0, 1, 0, -1, 0]
#
# INF = float('inf')
# dist = [[INF] * m for _ in range(n)]
#
# queue = deque()
# queue.append((sx, sy, 0))
# dist[sx][sy] = 0
#
# while queue:
#     x, y, step = queue.popleft()
#     if x == ex and y == ey:
#         print(step)
#         break
#     for i in range(4):
#         for j in range(1, k + 1):
#             nx = x + direc[i] * j
#             ny = y + direc[i+1] * j
#             if not (0 <= nx < n and 0 <= ny < m):
#                 break
#             if maze[nx][ny] == '#':
#                 break
#
#             if dist[nx][ny] > step + 1:
#                 dist[nx][ny] = step + 1
#                 queue.append((nx, ny, step + 1))
#
# print(-1 if dist[ex][ey] == INF else dist[ex][ey])

# https://codeforces.com/contest/2121/problem/A
# t = int(input())
# for _ in range(t):
#     n, s= map(int, input().split())
#     arr = list(map(int, input().split()))
#     if n == 1:
#         print(abs(s - arr[0]))
#         continue
#     else:
#         if arr[0] < s < arr[-1]:
#             mini1 = abs(s - arr[0])
#             mini2 = abs(arr[-1] - s)
#             mini = min(mini1, mini2)
#             maxi = max(mini1, mini2)
#             print(2*mini + maxi)
#         elif arr[0] >= s:
#             print(arr[-1]-s)
#             continue
#         elif s >= arr[-1]:
#             print(s-arr[0])
#             continue


# https://codeforces.com/contest/2121/problem/B
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     freq = Counter(s)
#     flag = False
#     for i in range(1, n-1):
#         if freq[s[i]] > 1:
#             flag = True
#     if flag:
#         print('YES')
#     else:
#         print('NO')

#bruteforce approach
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()
#     found = False
#     # Try all valid positions for b (must be at least 1 character, and leave room for a and c)
#     for i in range(1, n - 1):
#         for j in range(i + 1, n):
#             a = s[:i]
#             b = s[i:j]
#             c = s[j:]
#             if b in (a + c):
#                 found = True
#                 break
#         if found:
#             break
#     print("Yes" if found else "No")

# t = int(input())
# for _ in range(t):
#     a, x, y = map(int, input().split())
#     found = False
#     for b in range(1, 101):
#         if b == a:
#             continue
#         if abs(b - x) < abs(a - x) and abs(b - y) < abs(a - y):
#             found = True
#             break
#     print("YES" if found else "NO")

