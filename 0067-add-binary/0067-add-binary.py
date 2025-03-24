class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        a_len = len(a)-1
        b_len = len(b)-1
        while(a_len>=0 or b_len>=0 or carry): # "or carry" means carry isn't zero. so we add this
            if a_len>=0 :
                carry += int(a[a_len])
                a_len -= 1
            if b_len >= 0:
                carry += int(b[b_len])
                b_len -= 1
            result += str(carry % 2)
            carry  //= 2
        return result[::-1]
        