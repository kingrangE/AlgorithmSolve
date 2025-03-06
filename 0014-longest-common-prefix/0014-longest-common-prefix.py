class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0
        output = ''
        while True :
            try :
                c = strs[0][idx] # character of first string
                for string in strs :
                    if string[idx] != c :
                        return output
            except :
                return output
            output += c
            idx += 1
