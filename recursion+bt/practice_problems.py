#method 1, if given string.
#1. Backtracking style - approach 1

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }

def helper(ans, idx, curr, digits):
    if idx == len(digits):
        ans.append(curr)
        return

    letters = d[digits[idx]]
    for ch in letters:
        helper(ans, idx+1, curr + ch, digits)

def letterCombinations(digits: str):
    if not digits:
        return []
    ans = []
    helper(ans, 0, '', digits)
    return ans

print((letterCombinations('23')))

#return style - 2nd approach.
class Solution:
    def helper(self, idx, curr, digits):
        if idx == len(digits):
            return [curr]

        letters = d[digits[idx]]
        ans = []
        for ch in letters:
            ans += self.helper(idx+1, curr + ch, digits)
        return ans

    def letterCombinations(self, digits: str):
        if not digits:
            return []
        return self.helper(0, '', digits)


# method 2, if given an integer

mapping = {
    2: 'abc', 3: 'def', 4: 'ghi',
    5: 'jkl', 6: 'mno', 7: 'pqrs',
    8: 'tuv', 9: 'wxyz'
}

def keypad(n):
    if n == 0:
        return ['']

    smallInt = n // 10
    lastInt = n % 10

    smallOutput = keypad(smallInt)  # recursively get combinations for earlier digits
    lastdigitChars = mapping[lastInt]

    output = []
    for ch in lastdigitChars:
        for item in smallOutput:
            output.append(item + ch)
    return output

print(keypad(23))

# n = number of digits in the input

# | Approach       | Time Complexity | Space Complexity      | Notes                                         |
# | -------------- | --------------- | --------------------- | --------------------------------------------- |
# | Method 1       | O(4^n × n)      | O(4^n × n)            | Efficient in-place with less auxiliary memory |
# | Method 2       | O(4^n × n)      | O(4^n × n) (more aux) | Cleaner logic, more memory overhead           |


