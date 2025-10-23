from typing import  List

# def count_paths(grid, m, n):
#     if m == 1 or n == 1:
#         return 1
#
#     up = count_paths(grid, m-1, n)
#     left = count_paths(grid, m, n-1)
#     return up + left
# grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# print(count_paths(grid, 3, 4))


# counter = 1
# def print_paths(grid, m, n, path):
#     if m == 1 and n == 1:
#         global counter
#         print(path, counter)
#         counter += 1
#         return
#     if m > 1:
#         print_paths(grid, m-1, n, path+'D')
#     if n > 1:
#         print_paths(grid, m, n-1, path+'R')
#
# grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# # m = row, n = col
# print_paths(grid, 3, 4, '')


# def return_paths(grid, m, n, path):
#     if m == 1 and n == 1:
#         return [path]
#     down, ryt = [], []
#     if m > 1:
#         down = return_paths(grid, m-1, n, path+'D')
#     if n > 1:
#         ryt =return_paths(grid, m, n-1, path+'R')
#     return down + ryt
#
# grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# # m = row, n = col
# print(return_paths(grid, 3, 4, ''))



#all directions - 4

# def helper_print_all_paths(x, y, rows, cols, vis, curr):
#     if x == rows - 1 and y == cols - 1:
#         print(curr)
#         return
#
#     if x < 0 or x >= rows or y < 0 or y >= cols or vis[x][y] == 1:
#         return
#
#     vis[x][y] = 1
#     helper_print_all_paths(x + 1, y, rows, cols, vis, curr + 'D')  # Down
#     helper_print_all_paths(x, y + 1, rows, cols, vis, curr + 'R')  # Right
#     helper_print_all_paths(x - 1, y, rows, cols, vis, curr + 'U')  # Up
#     helper_print_all_paths(x, y - 1, rows, cols, vis, curr + 'L')  # Left
#     vis[x][y] = 0
#
# def print_all_paths(m, n):
#     vis = [[0 for _ in range(n)] for _ in range(m)]
#     helper_print_all_paths(0, 0, m, n, vis, '')
#
# print_all_paths(3,4)


# def helper_paths(x, y, rows, cols, vis, curr, path, step):
#     if x == rows - 1 and y == cols - 1:
#         path[x][y] = step
#         for arr in path:
#             print(arr)
#         print(curr)
#         print()
#         return
#
#     if x < 0 or x >= rows or y < 0 or y >= cols or vis[x][y] == 1:
#         return
#
#     vis[x][y] = 1
#     path[x][y] = step
#     helper_paths(x + 1, y, rows, cols, vis, curr + 'D', path, step + 1)  # Down
#     helper_paths(x, y + 1, rows, cols, vis, curr + 'R', path, step + 1)  # Right
#     helper_paths(x - 1, y, rows, cols, vis, curr + 'U', path, step + 1)  # Up
#     helper_paths(x, y - 1, rows, cols, vis, curr + 'L', path, step + 1)  # Left
#     vis[x][y] = 0
#     path[x][y] = 0
#
# def print_path_grid(m,n):
#     path = [[0]*n for _ in range(m)]
#     vis = [[0 for _ in range(n)] for _ in range(m)]
#     helper_paths(0, 0, m, n, vis, '', path, 1)
#
# print_path_grid(3,3)




# from typing import List
#
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         n = len(s)
#         self.helper(s, res, [], 0, n)
#         return res
#
#     def helper(self, s: str, res: List[List[str]], curr: List[str], idx: int, n):
#         if idx == n:
#             res.append(curr[:])
#             # print(res)
#             return
#
#         for i in range(idx, n):
#             small = s[idx:i+1]
#             print(small, idx, curr)
#             if small == small[::-1]:
#                 curr.append(small)
#                 self.helper(s, res, curr, i+1, n)
#                 curr.pop()
#
# st = 'aab'
# s = Solution()
# print(s.partition(st))


# def is_safe(row, col, n, board):
#     directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2)]
#     for dr, dc in directions:
#         r, c = row + dr, col + dc
#         if 0 <= r < n and 0 <= c < n and board[r][c] == 'K':
#             return False
#     return True
#
# def helper_nknights(row, n, board):
#     if row == n:
#         print([''.join(r) for r in board])
#         print()
#         return
#
#     for col in range(n):
#         if is_safe(row, col, n, board):
#             board[row][col] = 'K'
#             helper_nknights(row + 1, n, board)
#             board[row][col] = '.'
#
# def n_knights(n):
#     board = [['.'] * n for _ in range(n)]
#     helper_nknights(0, n, board)
#
# n_knights(3)

# def is_safe_suduko(board, row, col, num, n):
#     #check row
#     for i in range(n):
#         if board[row][i] == str(num):
#             return False
#
#     #check col
#     for i in range(n):
#         if board[i][col] == str(num):
#             return False
#
#     #check that 3*3 grid.
#     sqrt = int(n**(0.5))
#     start_row = row - (row)%sqrt
#     start_col = col - (col)%sqrt
#     for i in range(start_row, row+start_row):
#         for j in range(start_col,col+start_col):
#             if board[i][j] == str(num):
#                 return False
#     return True
#
# def helper_suduko(board, n):
#     for i in range(n):
#         for j in range(len(board[0])):
#             if board[i][j] == '.':
#                 for num in range(1,10):
#                     if is_safe_suduko(board, i, j, num, n):
#                         board[i][j] = str(num)
#                         if helper_suduko(board,n):
#                             return True
#                         board[i][j] = '.'
#                 return False
#     return True
#
#
# def sudukoSolver(board):
#     helper_suduko(board, len(board))
#     return board



# class Solution:
#     def initialize(self,board):
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]!=".":
#                     self.row[i].add(board[i][j])
#                     self.col[j].add(board[i][j])
#                     self.box[(i//3)*3+(j//3)].add(board[i][j])
#                 else:
#                     self.empty.append((i,j))
#     def solve(self,board,index):
#         if index==len(self.empty):
#             return True
#         i,j=self.empty[index]
#
#
#         for c in "123456789":
#             if self.isSafe(i,j,c):
#                 board[i][j]=c
#                 self.row[i].add(c)
#                 self.col[j].add(c)
#                 self.box[(i//3)*3+(j//3)].add(c)
#                 if self.solve(board,index+1):
#                     return True
#                 board[i][j]="."
#                 self.row[i].remove(c)
#                 self.col[j].remove(c)
#                 self.box[(i//3)*3+(j//3)].remove(c)
#         return False
#
#     def isSafe(self,i,j,c):
#         if c in self.row[i] or c in self.col[j] or c in self.box[(i//3)*3+(j//3)]:
#             return False
#         return True
#
#     def solveSudoku(self, board) -> None:
#         self.row=[set() for _ in range(9)]
#         self.col=[set() for _ in range(9)]
#         self.box=[set() for _ in range(9)]
#         self.empty=[]
#         self.initialize(board)
#         self.solve(board,0)
#
# board = [
#         ["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]
#     ]
#
# s = Solution()
# s.solveSudoku(board)
# for r in board:
#     print(*r)

# class Solution:
#     def helper(self, n, curr, open_c, close_c, ans):
#         if len(curr) == 2*n:
#             ans.append(''.join(curr))
#             return
#         if open_c < n:
#             curr.append('(')
#             self.helper(n, curr, open_c+1, close_c, ans)
#             curr.pop()
#         if open_c > close_c:
#             curr.append(')')
#             self.helper(n, curr, open_c, close_c+1, ans)
#             curr.pop()
#     def generateParenthesis(self, n: int):
#         ans = []
#         self.helper(n, [], 0, 0, ans)
#         return ans

# s = Solution()
# s.generateParenthesis(3)


# https://leetcode.com/problems/expression-add-operators/description/
# class Solution:
#     def addOperators(self, num: str, target: int):
#         ans = []
#         n = len(num)
#         curr = num[0]
#         self.helper(curr, ans, target, num, 0, 1, n)
#         return ans
#
#     def helper(self, temp, ans, target, num, curr, idx, n):
#         if idx == n:
#             if curr == target:
#                 ans.append(temp)
#             return
#         if curr > target:
#             return
#
#         for i in range(idx, n):
#             val = int(num[i])
#             self.helper(temp+'+'+num[i], ans, target, num, curr+val, i+1, n)
#             self.helper(temp+'-'+num[i], ans, target, num, curr-val, i+1, n)
#             self.helper(temp+'*'+num[i], ans, target, num, curr*val, i+1, n)
#

# https://leetcode.com/problems/letter-tile-possibilities/description/
# class Solution:
#     def numTilePossibilities(self, tiles: str) -> int:
#         sequences = set()
#         used = [False] * len(tiles)
#         # Generate all possible sequences including empty string
#         self._generate_sequences(tiles, "", used, sequences)
#         # Subtract 1 to exclude empty string from count
#         return len(sequences) - 1
#
#     def _generate_sequences(self, tiles: str, current: str, used: list, sequences: set) -> None:
#         sequences.add(current)
#
#         # Try adding each unused character to current sequence
#         for pos, char in enumerate(tiles):
#             if not used[pos]:
#                 used[pos] = True
#                 self._generate_sequences(tiles, current + char, used, sequences)
#                 used[pos] = False
#
# s = Solution()
# print(s.numTilePossibilities('AB'))


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }


#appraoch 1: in the base case our strings is formed so append to our ans
#backtrack in for loop. do, explore , undo

# class Solution:
#     def letterCombinations(self, digits):
#         if not digits:
#             return []
#         ans = []
#         self.helper(0, [], digits, ans)
#         return ans
#
#     def helper(self, idx, curr, s, ans):
#         if idx == len(s):
#             ans.append(''.join(curr))
#             return
#
#         chars = d[s[idx]]
#         for ch in chars:
#             curr.append(ch)
#             self.helper(idx+1, curr, s, ans)
#             curr.pop()

#approach 2: instead of adding the ans to same list, create new list each time and add ans to that list instead.
# class Solution:
#     def letterCombinations(self, digits):
#         if not digits:
#             return []
#         return self.helper(0, [], digits)
#
#     def helper(self, idx, curr, s):
#         if idx == len(s):
#             return [''.join(curr)]
#         ans = []
#         chars = d[s[idx]]
#         for ch in chars:
#             curr.append(ch)
#             ans += self.helper(idx+1, curr, s)
#             curr.pop()
#         return ans
#
# digits = '23'
# s = Solution()
# print(s.letterCombinations(digits))



# class Solution:
#      def solveNQueens(self, n: int) -> List[List[str]]:
#           board = [['.']*n for _ in range(n)]
#           ans = []
#           self.helper_nQueens(0,ans, board,n, set(), set(), set())
#           return ans
#
#      def helper_nQueens(self, row, ans, board, n, up, left_diag, ryt_diag):
#           if row == n:
#                # print(board)
#                ans.append([''.join(r) for r in board])
#                return
#
#           for col in range(n):
#                if col not in up and row+col not in ryt_diag and row-col not in left_diag:
#                     board[row][col] = 'Q'
#                     up.add(col)
#                     left_diag.add(row-col)
#                     ryt_diag.add(row+col)
#                     self.helper_nQueens(row+1, ans, board, n, up, left_diag, ryt_diag)
#                     board[row][col] = '.'
#                     up.remove(col)
#                     left_diag.remove(row-col)
#                     ryt_diag.remove(row+col)
#
# s = Solution()
# print(s.solveNQueens(4))



# class Solution:
#      def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#           ans = []
#           temp = []
#           candidates.sort()
#           n = len(candidates)
#           self.helper(temp, ans, candidates, target, n, 0)
#           return ans
#
#      def helper(self, temp, ans, nums, target, n, idx):
#           if idx == n:
#                if target == 0:
#                     ans.append(temp[:])
#                return
#
#           if target < 0:
#                return
#
#           temp.append(nums[idx])
#           self.helper(temp, ans, nums, target-nums[idx], n, idx+1)
#           temp.pop()
#
#           while idx+1 < n and nums[idx+1] == nums[idx]:
#                idx = idx+1
#
#           self.helper(temp, ans, nums, target, n, idx+1)
#
#
# candidates = [10,1,2,7,6,1,5]
# target = 8
# s = Solution()
# print(s.combinationSum2(candidates, target))


class Solution:
     def ratInMaze(self, maze):
          n = len(maze)
          ans = []
          temp = ''
          self.helper(ans, temp, n, maze, 0, 0)
          return ans

     def helper(self, ans, temp, n, maze, r, c):
          if r >= n or r < 0 or c >= n or c < 0 or maze[r][c] != 0:
               return

          if r == n-1 and c == n-1:
               # print(temp)
               ans.append(temp)
               return

          maze[r][c] = 0
          self.helper(ans, temp+'R', n, maze, r+1, c)
          self.helper(ans, temp+'L', n, maze, r-1, c)
          self.helper(ans, temp+'D', n, maze, r, c+1)
          self.helper(ans, temp+'U', n, maze, r, c-1)
          maze[r][c] = 1
# class Solution:
#      def ratInMaze(self, maze):
#           n = len(maze)
#           ans = []
#           temp = ''
#           self.helper(ans, temp, n, maze, 0, 0)
#           return ans
#
#      def helper(self, ans, temp, n, maze, r, c):
#           if r >= n or r < 0 or c >= n or c < 0 or maze[r][c] == 0:
#                return
#
#           if r == n-1 and c == n-1:
#                ans.append(temp[:])
#                return
#
#           maze[r][c] = 0
#           self.helper(ans, temp+'R', n, maze, r+1, c)
#           self.helper(ans, temp+'L', n, maze, r-1, c)
#           self.helper(ans, temp+'D', n, maze, r, c+1)
#           self.helper(ans, temp+'U', n, maze, r, c-1)
#           maze[r][c] = 1

mat= [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
s = Solution()
print(s.ratInMaze(mat))














