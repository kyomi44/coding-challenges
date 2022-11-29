class Solution:
    def isPalindrome(self, x: int) -> bool:

        for i in range(0, int(len(str(x))/2)):
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                return False
        return True
