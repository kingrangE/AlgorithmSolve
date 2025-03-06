class Solution:
    def romanToInt(self, s: str) -> int:
        l = ['I','V','X','L','C','D','M']
        M = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # t번째 단어의 index가 t+1번째 단어의 index보다 작다면 V(t+1) - V(t)
        # 같다면 V(t+1)+V(t)
        # 크다면 V
        output = 0
        last_roman = ''
        for roman in s :
            if last_roman == 'C' and roman == 'D': output += 300
            elif last_roman == 'C' and roman == 'M': output += 800
            elif last_roman == 'X' and roman == 'L': output += 30
            elif last_roman == 'X' and roman == 'C': output += 80
            elif last_roman == 'I' and roman == 'V': output += 3
            elif last_roman == 'I' and roman == 'X' : output += 8
            else : output += M[roman]
            last_roman = roman
        return output
