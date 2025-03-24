class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # sol 1 -> transform binary into desimal (easy)
        # sol 2 -> 2's complement method for adding nums
        def transform_to_decimal(num: str) -> int:
            result = 0 
            length = len(num) - 1
            for idx in range(length, -1, -1) : 
                result+= int(num[idx]) * 2**(length-idx)
            return result

        def transform_to_binary(num: int) -> str:
            result = ""
            while(True):
                if num %2 == 0:
                    result += "0"
                else :
                    result += "1"
                num //= 2
                if num == 0 : break
            return result[::-1]
        a = transform_to_decimal(a)
        b = transform_to_decimal(b)
        result = transform_to_binary(a + b)
        return result

        