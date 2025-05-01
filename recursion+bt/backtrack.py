from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        self.helper(s, res, [], 0, n)
        return res
    
    def helper(self, s: str, res: List[List[str]], curr: List[str], idx: int, n):
        if idx == n:
            res.append(curr[:])
            # print(res)
            return

        for i in range(idx, n):
            small = s[idx:i+1]
            print(small, idx, curr)
            if small == small[::-1]:
                curr.append(small)
                self.helper(s, res, curr, i+1, n)
                curr.pop()

st = 'aab'
s = Solution()
print(s.partition(st))