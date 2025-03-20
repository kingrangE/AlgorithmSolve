import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pattern = '[a-zA-Z]+'
        return len(re.findall(pattern,s)[-1])
        