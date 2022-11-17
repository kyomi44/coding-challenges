# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        highn = n
        lown = 0


        while(guess(n)!= 0):
            if(guess(n) == -1):
                if(highn > n):
                    highn = n
                elif(((highn - lown)%2) == 0):
                    n = (highn - lown)/2 + lown
                else:
                    n = (highn - lown - 1)/2 + lown
            else:
                if(lown < n):
                    lown = n
                elif(((highn - lown)%2) == 0):
                    n = lown + ((highn - lown)/2)
                else:
                    n = lown + ((highn - lown - 1)/2)
        
        return int(n)
