class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        ans = ''
        
        for n in range(len(s)-1, -1, -1):
            if ord(s[n]) != 32:
                stack.append(s[n])
            elif stack:
                while stack:
                    ans += stack.pop()
                ans += " "
        while stack:
            ans+= stack.pop()
        if ans[len(ans)-1] == " ":
            ans = ans[:-1]
        
        return ans
                