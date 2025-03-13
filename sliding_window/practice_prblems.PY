

# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        n = len(blocks)
        ans = float('inf')
        whites = 0 
        blacks = 0
        while j < n:
            if blocks[j] == 'W':
                whites += 1
            elif blocks[j] == 'B':
                blacks += 1
            while j-i+1>=k:
                ans = min(whites, ans)
                if blocks[i] == 'W':
                    whites -= 1
                else:
                    blacks -= 1
                i+=1
            j += 1
        return ans


# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)
        right = 0
        while right < n:
            char_count[s[right]] += 1
            
            while char_count['a'] > 0 and \
                char_count['b'] > 0 and char_count['c'] > 0:
                count += n - right
                char_count[s[left]] -= 1
                left += 1
            right += 1
        return count