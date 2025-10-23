# class Solution:
#     def printLCS(self, s1: str, s2: str) -> str:
#         n1, n2 = len(s1), len(s2)
#         dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
#
#         # Build the DP table
#         for i in range(1, n1 + 1):
#             for j in range(1, n2 + 1):
#                 if s1[i - 1] == s2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#         # Backtrack to find the LCS
#         i, j = n1, n2
#         lcs = []
#         while i > 0 or j > 0:
#             if s1[i - 1] == s2[j - 1]:
#                 lcs.append(s1[i - 1])
#                 i -= 1
#                 j -= 1
#             elif dp[i - 1][j] > dp[i][j - 1]:
#                 lcs.append(s1[i - 1])
#                 i -= 1
#             else:
#                 lcs.append(s2[j - 1])
#                 j -= 1
#
#         print(i,j)
#         return ''.join(reversed(lcs))
#
#
# s1 = 'abac'
# s2 = 'cab'
# s = Solution()
# print(s.printLCS(s1, s2))
#
#
#
# class Solution:
#     def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
#         n1 = len(s1)
#         n2 = len(s2)
#         dp = [[0]*(n2+1) for _ in range(n1+1)]
#
#         for i in range(1, n1+1):
#             for j in range(1, n2+1):
#                 if s1[i-1] == s2[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
#         i, j = n1, n2
#         lcs = []
#         while i > 0 and j > 0:
#             if s1[i - 1] == s2[j - 1]:
#                 lcs.append(s1[i - 1])
#                 i -= 1
#                 j -= 1
#             elif dp[i - 1][j] > dp[i][j - 1]:
#                 i -= 1
#             else:
#                 j -= 1
#
#         return ''.join(reversed(lcs))

for i in range(26):
    ch = chr(97+i)
    print(ch)