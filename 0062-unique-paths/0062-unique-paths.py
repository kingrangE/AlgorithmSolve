class Solution:
    def factorial(n):
        result = 1
        for i in range(1,n):
            result *= i+1
        return result

    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))