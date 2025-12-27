class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return lcp
            lcp += strs[0][i]
        return lcp
        
            



'''
Index first, character second
Think: “position i” → then “what character is at i in each word”.

Stop early
The moment one word:

runs out of characters, or

has a different character
you stop and return what you’ve built so far.
'''
