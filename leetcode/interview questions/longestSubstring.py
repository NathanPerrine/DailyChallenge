def lengthOfLongestSubstring(s: str) -> int:
        seen = {}
        l = 0
        output = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output, r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output, r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

# 61 ms, https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation
# Time: O(n), n = length of string, iterate over string n times
# Time: O(m), m = unique characters stored in dict
