class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        if s[left+1] == s[right]:  # delete the left char
            sub = s[left+1:right+1]
            if sub == sub[::-1]:
                return True
        if s[left] == s[right-1]:  # delete the right char
            sub = s[left:right]
            if sub == sub[::-1]:
                return True
        return False
