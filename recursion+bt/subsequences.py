
# Print subsets of a string
# def helper_print_subsets(s, idx, curr):
#     if idx == len(s):
#         print(curr, 'curr')
#         return
#
#     ch = s[idx]
#     helper_print_subsets(s, idx + 1, curr+ch) #take
#     helper_print_subsets(s, idx + 1, curr) #not take
#
# def print_subsets(s):
#     helper_print_subsets(s, 0, '')
#
# print_subsets('abc')



#Return list of subsets

# def helper_subsets_return_m1(ans, temp, s, idx):
#     if idx == len(s):
#         ans.append(temp[:])
#         return
#
#     helper_subsets_return_m1(ans, temp+s[idx], s, idx+1)
#     helper_subsets_return_m1(ans, temp, s, idx+1)
#
# def subsets_string_return_method1(s):
#     ans = []
#     helper_subsets_return_m1(ans, '', s, 0)
#     return ans
#
# print(subsets_string_return_method1('abc'))



# def helper_subsets_return_m2(s, idx, ans):
#     if idx == len(s):
#         return [ans]
#
#     ch = s[idx]
#     take = helper_subsets_return_m2(s, idx + 1, ans + ch)
#     not_take = helper_subsets_return_m2(s, idx + 1, ans)
#     return take + not_take
#
# def subsets_string_return_method2(s):
#     return helper_subsets_return_m2(s, 0, '')
#
# print(subsets_string_return_method2('abc'))



#2. print/return subsequence without duplicates

#method 1

# def helper_subsequences_without_dup(s, idx, curr):
#     if idx == len(s):
#         print(curr, 'here')
#         return
#     # Take s[idx]
#     helper_subsequences_without_dup(s, idx + 1, curr + s[idx])
#     # Not take s[idx], and skip all its duplicates
#     while idx + 1 < len(s) and s[idx] == s[idx + 1]:
#         idx += 1
#     helper_subsequences_without_dup(s, idx + 1, curr)
#
# def print_subsequences_without_dup1(s):
#     s = ''.join(sorted(s))  # sort to group duplicates
#     helper_subsequences_without_dup(s, 0, '')
#
# # print_subsequences_without_dup1('aab')

# def helper_subsequences_without_dup(s, idx, curr):
#     if idx == len(s):
#         print(curr)
#         return
#     helper_subsequences_without_dup(s, idx+1, curr+s[idx])
#     while idx+1 < len(s) and  s[idx+1] == s[idx]:
#         idx += 1
#     helper_subsequences_without_dup(s, idx+1, curr)
#
# def print_subsequences_without_dup1(s):
#     s = ''.join(sorted(s))  # sort to group duplicates
#     helper_subsequences_without_dup(s, 0, '')
#
# print_subsequences_without_dup1('aab')


# # method 2

# def helper_subsequences_unique(s, idx, curr):
#     print(curr)  # print at every leaf node
#
#     for i in range(idx, len(s)):
#         # Skip duplicates at the same level
#         if i > idx and s[i] == s[i - 1]:
#             continue
#         helper_subsequences_unique(s, i + 1, curr + s[i])
#
# def print_subsequences_without_dup2(s):
#     s = ''.join(sorted(s))  # Sorting to group duplicates
#     helper_subsequences_unique(s, 0, '')
#
# print_subsequences_without_dup2('aab')


#Return subsequences without duplicates

# def helper_return_subsequences_without_dup1(s, idx, curr):
#     if idx == len(s):
#         return [curr]
#     # Take s[idx]
#     take = helper_return_subsequences_without_dup1(s, idx + 1, curr + s[idx])
#     # Not take s[idx], and skip all its duplicates
#     while idx + 1 < len(s) and s[idx] == s[idx + 1]:
#         idx += 1
#     not_take = helper_return_subsequences_without_dup1(s, idx + 1, curr)
#     return take + not_take
#
# def return_subsequences_without_dup1(s):
#     s = ''.join(sorted(s))  # sort to group duplicates
#     return helper_return_subsequences_without_dup1(s, 0, '')
#
# print(return_subsequences_without_dup1('aab'))

#method 2
# def helper_return_subsequences_without_dup2(s, idx, curr, ans):
#     if idx == len(s):
#         ans.append(curr)
#         return
#     # Take s[idx]
#     helper_return_subsequences_without_dup2(s, idx + 1, curr + s[idx], ans)
#     # Not take s[idx], and skip all its duplicates
#     while idx + 1 < len(s) and s[idx] == s[idx + 1]:
#         idx += 1
#     helper_return_subsequences_without_dup2(s, idx + 1, curr, ans)
#
#
# def return_subsequences_without_dup2(s):
#     # print(sorted(s), 'here')
#     s = ''.join(sorted(s))  # sort to group duplicates
#     ans = []
#     helper_return_subsequences_without_dup2(s, 0, '', ans)
#     return ans
#
# print(return_subsequences_without_dup2('aacb'))



# Print permutations

# def helper_print_perm(s, used, curr):
#     if len(curr) == len(s):
#         print(curr)
#         return
#
#     for i in range(len(s)):
#         if not used[i]:
#             used[i] = True
#             helper_print_perm(s, used, curr + s[i])
#             used[i] = False  # backtrack
#
# def print_perm(s):
#     used = [False] * len(s)
#     helper_print_perm(s, used, '')
#
# print_perm('abc')


# def helper_print_perm(s, idx):
#     if idx == len(s):
#         print(''.join(s))
#         return
#
#     for i in range(idx, len(s)):
#         s[idx], s[i] = s[i], s[idx]      # swap
#         helper_print_perm(s, idx + 1)
#         s[idx], s[i] = s[i], s[idx]      # backtrack
#
# def print_perm(s):
#     chars = list(s)
#     helper_print_perm(chars, 0)
#
# print_perm('abc')


#Return permutations

#method 1

# def helper_return_perm1(s, ans, idx):
#     if idx == len(s):
#         st = ''.join(s[:])
#         ans.append(st)
#         return
#
#     for i in range(idx, len(s)):
#         s[i] , s[idx] = s[idx], s[i]
#         helper_return_perm1(s, ans, idx+1)
#         s[idx] , s[i] = s[i], s[idx]
#
# def return_permutations1(s):
#     ans = []
#     s = list(s)
#     helper_return_perm1(s, ans, 0)
#     return  ans
#
# print(return_permutations1('abc'))


#method 2
# def helper_return_perm2(s, idx):
#     if idx == len(s):
#         return [''.join(s[:])]
#
#     res = []
#     for i in range(idx, len(s)):
#         s[i], s[idx] = s[idx], s[i]           # swap
#         res += helper_return_perm2(s, idx + 1)  # collect
#         s[idx], s[i] = s[i], s[idx]           # backtrack
#     return res
#
# def return_permutations2(s):
#     s = list(s)
#     return helper_return_perm2(s, 0)
#
# print(return_permutations2('abc'))

# Return count of permutations.

# def helper_return_perm2(s, idx):
#     if idx == len(s):
#         return 1
#
#     res = 0
#     for i in range(idx, len(s)):
#         s[i], s[idx] = s[idx], s[i]           # swap
#         res +=  helper_return_perm2(s, idx + 1)  # collect
#         s[idx], s[i] = s[i], s[idx]           # backtrack
#     return res
#
# def return_permutations2(s):
#     s = list(s)
#     return helper_return_perm2(s, 0)
#
# print(return_permutations2('abcde'))

