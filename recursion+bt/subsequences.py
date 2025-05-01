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


def helper_subsets(ans, temp, s, idx):
    if idx == len(s):
        ans.append(temp[:])
        return
    
    helper_subsets(ans, temp+s[idx], s, idx+1)
    helper_subsets(ans, temp, s, idx+1)

def subsets_string(s):
    ans = []
    helper_subsets(ans, '', s, 0)
    return ans

# def helper_subsets(s, idx, ans):
#     if idx == len(s):
#         return [ans]
    
#     ch = s[idx]
#     take = helper_subsets(s, idx + 1, ans + ch)
#     not_take = helper_subsets(s, idx + 1, ans)
#     return take + not_take

# def subsets_string(s):
#     return helper_subsets(s, 0, '')
    
print(subsets_string('abc'))