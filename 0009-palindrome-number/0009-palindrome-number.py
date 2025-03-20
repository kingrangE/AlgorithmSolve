class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[-i-1] : 
                return False
        return True