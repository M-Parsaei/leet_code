class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            # negative numbers are not palindrome
            return False
        else:
            y = str(x)[::-1]
            if (x==int(y)):
                return True
            else:
                return False
        